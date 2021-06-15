from django.shortcuts import render
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
    permission_classes = [IsAuthenticated,]

    # get请求购物车
    def add(self,request):
        """"""
        course_id =request.data.get('course_id')

        user_id = request.user.id
        expire = 0 # 有效期 默认是0永久有效
        is_selected = True # 勾选状态 默认选中

        # 判断课程是否存在
        try:
            course_models.Course.objects.get(pk=course_id)

        except course_models.Course.DoesNotExist:
            return Response({'msg':'商品不存在，请重新选择'},status=status.HTTP_400_BAD_REQUEST)

        # todo 判断此用户是否已经添加过本课程
        try:
            redis_conn = get_redis_connection('cart')
            pipe = redis_conn.pipeline()
            pipe.multi()
            pipe.hset(f'cart_{user_id}',course_id,expire)
            pipe.sadd(f'select_{user_id}',course_id)
            pipe.execute()

            # 获取购物车的数量
            course_len = redis_conn.hlen(f'cart_{user_id}')
        except:
            logger.error('购物车添加失败')
            return Response({'msg':'购物车添加失败'},status=status.HTTP_507_INSUFFICIENT_STORAGE)
        return Response({'msg':'商品添加成功','course_len':course_len},status=status.HTTP_201_CREATED)

    # 获取购物车所有数据的接口
    def cart_list(self,request):

        user_id = request.user.id
        redis_conn = get_redis_connection('cart')

        # 取出所有课程数据
        cart_data_dict = redis_conn.hgetall(f'cart_{user_id}')

        # 取出所有选中课程id
        selected_course_data = redis_conn.smembers(f'select_{user_id}')
        # print('>>>>>',cart_data_dict)
        # print('>>>>>',selected_course_data)
        data = []
        course_len = redis_conn.hlen(f'cart_{user_id}')
        try:
            for course_id_bytes,expire_bytes in cart_data_dict.items():
                course_id = course_id_bytes.decode()
                expire_id = expire_bytes.decode()
                course_obj = course_models.Course.objects.get(pk=course_id)
                data.append({
                    "id":course_id,
                    "course_img":contants.SERVER_HOST + course_obj.course_img.url,
                    "name":course_obj.name,
                    "price":course_obj.price,
                    "expire_id":expire_id,
                    "is_selected":course_id_bytes in selected_course_data,
                })
        except:
            return Response({'msg': '课程获取失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'msg': data,'course_len':course_len}, status=status.HTTP_200_OK)
