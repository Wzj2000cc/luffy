from django.shortcuts import render

from rest_framework.generics import ListAPIView
from . import models,serializers
from luffyapi.settings import contants
# Create your views here.


class BannerAPIView(ListAPIView):
    """
    轮播图视图函数展示所有图片数据
    """
    queryset = models.Banner.objects.filter(is_deleted=False,is_show=True)[:contants.BANNER_LENGTH]
    serializer_class = serializers.BannerSerializers