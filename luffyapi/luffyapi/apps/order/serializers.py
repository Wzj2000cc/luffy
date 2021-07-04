from rest_framework import serializers
from . import models
from django_redis import get_redis_connection
from django.db import transaction
from datetime import datetime
from .models import Order,OrderDetail
from course.models import Course,CourseExpire
from coupon.models import UserCoupon
from users.models import User,Credit
from luffyapi.settings import contants


class OrderModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Order
        fields = ["id", "order_number", "pay_type", "credit", "coupon"]
        extra_kwargs = {
            "id": {"read_only": True},
            "order_number": {"read_only": True},
            "pay_type": {"write_only": True},
            "credit": {"write_only": True},
            "coupon": {"write_only": True}
        }

    def validate(self, attrs):

        # 校验数据
        # pay_type校验
        pay_type = attrs.get('pay_type')
        try:
            models.Order.pay_choices[pay_type]
        except:
            raise serializers.ValidationError('对不起，当前不支持选中的支付方式')

        # 判断优惠券是否满足使用条件，是否存在，或者是否已经过期
        user_coupon_id = attrs.get('coupon')

        # 判断用户是否使用了该优惠券
        if user_coupon_id > 0:
            try:
                # 判断用户有没有这个优惠券(并获取该优惠券)
                user_coupon = UserCoupon.objects.get(is_show=True,is_deleted=False,is_use=False,
                                                     user_id=self.context['request'].user.id,
                                                     pk = user_coupon_id)
            except:
                raise serializers.ValidationError('对不起，当前优惠券不可用或不存在')

            # 判断优惠券是否可用（在时间范围内）
            start_time = user_coupon.start_time.timestamp()
            end_time = user_coupon.end_time.timestamp()
            now_time = datetime.now().timestamp()
            if now_time < start_time or now_time > end_time:
                raise serializers.ValidationError('当前优惠券已过期')

        # 判断积分使用是否上限,总共200个，你发过来2000个，需要判断一下
        user_credit = self.context['request'].user.credit
        credit = attrs.get('credit',0)
        if credit > user_credit:
            raise serializers.ValidationError('对不起，当时使用积分超出上限')

        # todo 这里有可能订单生成了，但是他未支付，2个多月以后他才支付，但是这课程已经下架了

        return attrs

    # 将校验的数据保存到数据库
    def create(self, validated_data):

        # 生成订单号
        redis_conn = get_redis_connection('cart')

        # 获取自增数据(int类型)
        incr = redis_conn.incr('order')
        # print(f'数据类型{type(incr)}')

        # 获取时间戳
        time_now = datetime.now().strftime("%Y%m%d%H%M%S") # 202106241520

        # 获取用户身份标识 用户id
        # user_id = 7   # 测试使用用户id
        user_id = self.context['request'].user.id

        # 生成订单号
        order_number = time_now + '%06d' % incr + '%06d' % user_id

        pay_type = validated_data.get('pay_type')
        credit = validated_data.get('credit',0)
        coupon = validated_data.get('coupon',0)

        # 加入事务
        with transaction.atomic():
            save_id = transaction.savepoint() # 事务保存点，自动回滚到此处
            # 1. 生成订单表数据
            order = Order.objects.create(
                order_title = ' 路飞学城课程购买',
                total_price = 0,  # 积分未做，先给0
                real_price = 0,   # 积分未做，先给0
                order_number = order_number,  #订单号
                order_status = 0,   # 支付状态，未支付
                pay_type = pay_type,
                credit = credit,
                coupon = coupon,
                order_desc = '',
                user_id = user_id
            )

            # 2. 生成订单详情表数据

            # 取出所有课程数据
            cart_data_dict = redis_conn.hgetall(f'cart_{user_id}')

            # 获取所有选中的课程id
            selected_course_data = redis_conn.smembers(f'select_{user_id}')

            pipe = redis_conn.pipeline()
            pipe.multi()

            for course_id_bytes,expire_bytes in cart_data_dict.items():
                course_id = int(course_id_bytes.decode())
                expire_id = int(expire_bytes.decode())

                if course_id_bytes in selected_course_data:
                    try:  # 获取被选中的课程对象加入到结算页面
                        course = Course.objects.get(pk=course_id,is_show=True, is_deleted=False)
                    except Course.DoesNotExist:
                        continue

                    # 判断课程有效期，获取课程原价
                    original_price = course.price
                    try:
                        if expire_id > 0:  # 课程有效期id>0时，根据id找到courseexpire表对应的优惠价格
                            courseexpire = CourseExpire.objects.get(id = expire_id)
                            original_price = courseexpire.price
                    except CourseExpire.DoesNotExist:
                        pass

                    # 课程真实价格
                    real_price = course.real_price(expire_id)

                    OrderDetail.objects.create(
                        order=order,
                        course=course,
                        expire=expire_id,
                        price=original_price,
                        real_price=real_price,
                        discount_name=course.discount_name
                    )

                    # 计算订单的总价以及优惠后的价格("改"的操作)
                    order.total_price += float(original_price)
                    order.real_price += float(real_price)

                    # 移除已经加入到订单的购物车的商品
                    pipe.hdel(f'cart_{user_id}',course_id)
                    pipe.srem(f'select_{user_id}',course_id)

        # 保存Order订单记录的原价以及真实价格字段
        try:
            # 对总价加入优惠券折扣
            user_coupon_id = validated_data.get('coupon',0)
            if user_coupon_id > 0:
                user_coupon = UserCoupon.objects.get(is_show=True,
                                                     is_deleted=False,
                                                     is_use=False,
                                                     user_id=self.context['request'].user.id,
                                                     pk = user_coupon_id)
                if user_coupon.coupon.condition > order.real_price:
                    raise serializers.ValidationError('价格不满足')
                sale_num = float(user_coupon.coupon.sale[1:])
                if user_coupon.coupon.sale[0] == '*':
                    order.real_price *= sale_num
                elif user_coupon.coupon.sale[0] == '-':
                    order.real_price -= sale_num
                order.coupon = user_coupon_id


            # 对总价加入积分折扣
            if credit > 0:
                # 判断积分折合成钱大于该订单总价就抛出异常
                if credit > order.real_price * contants.CREDIT_MONEY:
                    transaction.savepoint_rollback(save_id)
                    raise serializers.ValidationError('订单生成失败，当前积分超过使用上限')
                order.real_price =float('%.2f' %(order.real_price - credit / contants.CREDIT_MONEY))
                order.credit = credit

                # todo 积分流水表添加相应数据
                if credit:
                    credit_obj = Credit.objects.create(
                        is_show=True,
                        is_deleted=False,
                        user_id = user_id,
                        number = credit,
                        opera = 2
                    )


            order.save()
            pipe.execute()
        except:
            transaction.savepoint_rollback(save_id)
            raise serializers.ValidationError('对不起，订单生成失败')
        # 返回生成的模型
        return order






