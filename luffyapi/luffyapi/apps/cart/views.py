from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ViewSet

# 引入redis数据库
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework import status
from course import models as course_models

# Create your views here.
import logging

logger = logging.getLogger('django')
class CartAPIView(ViewSet):

    def add(self,request):
        """"""
        course_id =request.data.get('course_id')

        # todo: user_id = request.user.id
        user_id = 1 # 虚构一个用户假id
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

            # 获取购物车的数量 =
            course_len = redis_conn.hlen(f'cart_{user_id}')
        except:
            logger.error('购物车添加失败')
            return Response({'msg':'购物车添加失败'},status=status.HTTP_507_INSUFFICIENT_STORAGE)
        return Response({'msg':'商品添加成功'},status=status.HTTP_201_CREATED)
