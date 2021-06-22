from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models,serializers
from luffyapi.settings import contants
# Create your views here.


""" 轮播图视图函数展示所有图片数据"""
class BannerAPIView(ListAPIView):

    queryset = models.Banner.objects.filter(is_deleted=False,is_show=True)[:contants.BANNER_LENGTH]
    serializer_class = serializers.BannerSerializers

""" 顶部导航栏视图函数展示所有图片数据"""
class HeaderNavAPIView(ListAPIView):

    queryset = models.Nav.objects.filter(is_deleted=False,is_show=True,position=1).order_by('orders')[:contants.HEADER_NAV_LENGTH]
    serializer_class = serializers.NavSerializers


# 底部导航栏视图函数展示所有图片数据
class BottomHeaderNavAPIView(ListAPIView):

    queryset = models.Nav.objects.filter(is_show=True,is_deleted=False,position=2).order_by('orders')[:contants.BANNER_LENGTH]
    serializer_class = serializers.NavSerializers