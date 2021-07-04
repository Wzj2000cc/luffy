from django.http import HttpResponse
from rest_framework.views import APIView
from alipay import AliPay,AliPayConfig
from luffyapi.settings.dev import ALIPAY_CONFIG
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from datetime import datetime

from order.models import Order
from coupon.models import UserCoupon
from course.models import CourseExpire
from users.models import UserCourse
# Create your views here.

""" 提供支付宝支付页面动态的url接口 """
class AlipayAPIView(APIView):

    def get(self,request):

        # 获取订单号
        order_number =request.query_params.get('order_number')

        try:
            order_obj = Order.objects.get(order_number=order_number)
        except Order.DoesNotExist:
            return Response({"message": "对不起,当前订单信息不存在!无法进行支付"}, status=status.HTTP_400_BAD_REQUEST)

        alipay = AliPay(
                appid = ALIPAY_CONFIG['appid'],
                app_notify_url = None,  # 默认回调 url
                app_private_key_string = open(ALIPAY_CONFIG['app_private_key_path']).read(),
                # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                alipay_public_key_string=open(ALIPAY_CONFIG["alipay_public_key_path"]).read(),
                sign_type = ALIPAY_CONFIG['sign_type'],  # RSA 或者 RSA2
                debug = ALIPAY_CONFIG['debug'],  # 默认 False
                verbose = ALIPAY_CONFIG['verbose'],  # 输出调试数据
                config=AliPayConfig(timeout=ALIPAY_CONFIG['timeout'])  # 可选，请求超时时间
            )

        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no = order_number, # 订单号
            total_amount = float(order_obj.real_price),  # 订单金额
            subject = order_obj.order_title,
            return_url=ALIPAY_CONFIG['return_url'],
            notify_url=ALIPAY_CONFIG['notify_url']  # 可选，不填则使用默认 notify url
        )

        # 支付成功后前端跳转的url
        url = ALIPAY_CONFIG["gateway_url"] + order_string
        return Response(url)

class AliPayResultAPIView(APIView):

    """
    处理支付宝同步通知结果的接口
    验证支付宝支付成功
    """
    def get(self,request):
        alipay = AliPay(
            appid=ALIPAY_CONFIG['appid'],
            app_notify_url=None,  # 默认回调 url
            app_private_key_string=open(ALIPAY_CONFIG["app_private_key_path"]).read(),
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=open(ALIPAY_CONFIG["alipay_public_key_path"]).read(),
            sign_type=ALIPAY_CONFIG['sign_type'],  # RSA 或者 RSA2
            debug=ALIPAY_CONFIG['debug'],  # 默认 False
            verbose=ALIPAY_CONFIG['verbose'],  # 输出调试数据
            config=AliPayConfig(timeout=ALIPAY_CONFIG['timeout'])  # 可选，请求超时时间
        )
        data = request.query_params.dict()
        signature = data.pop('sign')
        success = alipay.verify(data,signature)
        if success:
            res = self.change_order_status(data)
            return res
        return Response({'message':'对不起，支付失败~'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        alipay = AliPay(
            appid=ALIPAY_CONFIG['appid'],
            app_notify_url=None,  # 默认回调 url
            app_private_key_string=open(ALIPAY_CONFIG["app_private_key_path"]).read(),
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=open(ALIPAY_CONFIG["alipay_public_key_path"]).read(),
            sign_type=ALIPAY_CONFIG['sign_type'],  # RSA 或者 RSA2
            debug=ALIPAY_CONFIG['debug'],  # 默认 False
            verbose=ALIPAY_CONFIG['verbose'],  # 输出调试数据
            config=AliPayConfig(timeout=ALIPAY_CONFIG['timeout'])  # 可选，请求超时时间
        )
        data = request.data
        signature = data.pop('sign')
        success = alipay.verify(data,signature)
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            res = self.change_order_status(data)
            if res.status_code == 200:
                return HttpResponse('success')
        return Response({'message':'对不起，支付失败~'}, status=status.HTTP_400_BAD_REQUEST)


    def change_order_status(self,data):
        # 1. 更改订单状态，变成已支付
        order_number = data.get('out_trade_no')
        try:
            order = Order.objects.get(order_number=order_number,order_status=0)
        except Order.DoesNotExist:
            return Response({'message':'对不起，订单号不存在！'},status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                order.order_status = 1
                order.pay_time = datetime.now()
                order.save()

                # 2. 用户要更改使用的优惠券
                user_coupon_id = order.coupon
                if user_coupon_id:
                    user_coupon = UserCoupon.objects.get(pk=user_coupon_id,is_use=False)
                    user_coupon.is_use = True
                    user_coupon.save()

                # 3. 用户更改拥有的积分
                credit = order.credit
                if credit:
                    user = order.user
                    user.credit -= credit
                    user.save()

                # 4. 记录支付宝的流水号。（涉及到建表）
                # 用户购买记录表，一个用户购买一个课程就需要添加一条记录。我们现在已知的是订单对象。
                # 我们需要通过订单对象找到对应的所有的课程对象
                order_detail_list = order.order_courses.all()
                course_list = []
                for order_detail in order_detail_list:
                    course = order_detail.course
                    course.students += 1  # 生成订单该门课程学生人数应该加1
                    course.save()

                    # 5. 计算课程有效期
                    if order_detail.expire:
                        pay_timestamp = order.pay_time.timestamp()
                        expire = CourseExpire.objects.get(pk = order_detail.expire)
                        expire_timestamp = expire.expire_time *24 *60 *60
                        out_time = datetime.fromtimestamp(pay_timestamp + expire_timestamp)
                    else:
                        out_time = None

                    # 6. 添加购买记录
                    user = order.user
                    UserCourse.objects.create(
                        user_id = user.id,
                        course_id = course.id,
                        trade_no = data.get('trade_no'),
                        buy_type = 1,
                        pay_time = order.pay_time,
                        out_time = out_time,
                    )
                    course_list.append({
                        "id": course.id,
                        "name": course.name,
                    })
            except:
                transaction.savepoint_rollback(save_id)
                return Response({"message": "对不起，更新订单相关记录失败！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({
                'message': '支付成功，订单修改成功',
                "credit": user.credit,
                "pay_time": order.pay_time,
                "real_price": order.real_price,
                "course_list": course_list,
            }, status=status.HTTP_200_OK)