from django.shortcuts import render
from redis import RedisError
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ViewSet

# 引入redis数据库
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from course import models as course_models
from luffyapi.settings import contants
# Create your views here.
import logging

logger = logging.getLogger('django')


class CartAPIView(ViewSet):
    print('go!')

    """ 用户身份认证"""
    # permission_classes = [IsAuthenticated,]

    """post：detail课程详情页面将该课程加入购物车"""

    def add(self, request):

        course_id = request.data.get('course_id')
        user_id = request.user.id  # 获取当前登录用户的id
        expire = 0  # 有效期 默认是0永久有效

        # 判断课程是否存在
        try:
            course_models.Course.objects.get(pk=course_id)

        except course_models.Course.DoesNotExist:
            return Response({'msg': '商品不存在，请重新选择'}, status=status.HTTP_400_BAD_REQUEST)

        # todo 判断此用户是否已经添加过本课程
        try:
            redis_conn = get_redis_connection('cart')
            pipe = redis_conn.pipeline()
            pipe.multi()
            pipe.hset(f'cart_{user_id}', course_id, expire)
            pipe.sadd(f'select_{user_id}', course_id)
            pipe.execute()

            # 获取购物车里已添加课程的数量
            course_len = redis_conn.hlen(f'cart_{user_id}')
        except:
            logger.error('购物车添加失败')
            return Response({'msg': '购物车添加失败'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        return Response({'msg': '商品添加成功', 'course_len': course_len}, status=status.HTTP_201_CREATED)

    """ get：获取购物车所有购买的课程数据"""

    def cart_list(self, request):

        # user_id = request.user.id
        user_id = 1
        redis_conn = get_redis_connection('cart')

        # 取出所有课程数据
        cart_data_dict = redis_conn.hgetall(f'cart_{user_id}')

        # 取出所有选中课程id
        selected_course_data = redis_conn.smembers(f'select_{user_id}')
        data = []
        course_len = redis_conn.hlen(f'cart_{user_id}')
        try:
            for course_id_bytes, expire_bytes in cart_data_dict.items():
                course_id = course_id_bytes.decode()
                expire_id = expire_bytes.decode()
                course_obj = course_models.Course.objects.get(pk=course_id)
                data.append({
                    "id": course_id,
                    "course_img": contants.SERVER_HOST + course_obj.course_img.url,
                    "name": course_obj.name,
                    "price": course_obj.price,
                    "real_price": course_obj.real_price(int(expire_id)),
                    "expire_id": int(expire_id),
                    'expire_list': course_obj.expire_list,
                    "is_selected": course_id_bytes in selected_course_data,
                })
        except:
            return Response({'msg': '课程获取失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'msg': data, 'course_len': course_len}, status=status.HTTP_200_OK)

    """ patch请求：购物车页面商品修改勾选状态"""

    def change_course_selected(self, request):

        user_id = request.user.id
        course_id = request.data.get('course_id')
        is_selected = request.data.get('is_selected')

        try:
            course_models.Course.objects.get(pk=course_id)
        except course_models.Course.DoesNotExist:
            return Response({'msg': '商品不存在，请重新选择'}, status=status.HTTP_400_BAD_REQUEST)

        redis_conn = get_redis_connection('cart')
        if is_selected:
            redis_conn.sadd(f'select_{user_id}', course_id)
        else:
            redis_conn.srem(f'select_{user_id}', course_id)
        return Response({'msg': '勾选状态修改成功'}, status=status.HTTP_200_OK)

    """ put请求：购物车页面修改课程有效期状态"""

    def change_expire(self, request):

        user_id = request.user.id
        course_id = request.data.get('course_id')
        expire_id = request.data.get('expire_id')
        try:
            course_obj = course_models.Course.objects.get(pk=course_id)

            # 永久有效的记录没有在course—_expire这个表中，我们先要做排除
            if expire_id > 0:
                expire_obj = course_models.CourseExpire.objects.filter(is_show=True, is_deleted=False)

                if not expire_obj:
                    raise course_models.CourseExpire.DoesNotExist

            redis_conn = get_redis_connection('cart')
            redis_conn.hset(f'cart_{user_id}', course_id, expire_id)

        except course_models.CourseExpire.DoesNotExist:

            return Response({'msg': '有效期无效！'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception:

            return Response({'msg': '服务器内部错误！'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        real_price = course_obj.real_price(expire_id)
        return Response({'msg': '切换有效期选项成功！', 'real_price': real_price}, status=status.HTTP_200_OK)

    """ delete请求，删除购物车中课程数据 """

    def delete_course(self, request):

        user_id = request.user.id
        course_id = request.query_params.get('course_id')

        # 购物车前端点击删除选中会将选中的课程id发送到后端
        course_list = request.query_params.get('course_list')
        course_list = [course_id] if course_id else course_list.split(',')

        try:
            for course_id in course_list:
                course_models.Course.objects.get(pk=course_id)

                 # 利用redis事务处理redis的多次请求
                redis_conn = get_redis_connection('cart')
                pipe = redis_conn.pipeline()
                pipe.multi()
                pipe.hdel(f'cart_{user_id}', course_id)
                pipe.srem(f'select_{user_id}', course_id)
                pipe.execute()

        except course_models.Course.DoesNotExist:
            return Response({'msg': '商品不存在，请重新添加'}, status=status.HTTP_400_BAD_REQUEST)

        except RedisError:
            return Response({'msg': "服务器内部错误"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'msg': "删除商品成功"}, status=status.HTTP_204_NO_CONTENT)
