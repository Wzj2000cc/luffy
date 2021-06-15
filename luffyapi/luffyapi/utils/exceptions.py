from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError
from redis import RedisError

import logging

logger = logging.getLogger('django')



def custom_exception_handler(exc, context):


    response = exception_handler(exc,context)

    if response is None:
        view = context['view']
        if isinstance(exc,DatabaseError) or isinstance(exc,RedisError):
            # 记录日志
            logger.error(f'在[{view}]视图出现 [{exc}]错误')
            response = Response({'message':'服务器内部错误'},status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response