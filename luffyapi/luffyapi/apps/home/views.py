from django.shortcuts import render

from rest_framework.generics import ListAPIView
from . import models,serializers
from luffyapi.settings import contants
# Create your views here.


class BannerAPIView(ListAPIView):
    """
    轮播图视图函数展示所有图片数据
    """


    # /**
    # * showdoc
    # * @title 轮播图功能
    # * @description 轮播图前后端交互,前端获取后端传过来的图片路径
    # * @method get
    # * @url http://api.luffycity.cn:8001/home/banner
    # * @return [{"id": 1,"link": "https://www.cnblogs.com/jin-xin/p/9076242.html","image_url": "http://api.luffycity.cn:8001/media/banner/banner1.png"},{"id": 2,"link": "https://www.cnblogs.com/jin-xin/p/9076242.html","image_url": "http://api.luffycity.cn:8001/media/banner/banner2.png"}]
    # * @return_param name string Turbo
    # * @return_param link string 点击图片跳转的路径
    # * @return_param image_url string 图片路径
    # * @remark 轮播图接口文档
    # * @number 1
    # */


    queryset = models.Banner.objects.filter(is_deleted=False,is_show=True)[:contants.BANNER_LENGTH]
    serializer_class = serializers.BannerSerializers



