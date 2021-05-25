from rest_framework import serializers
from . import models

# 轮播图
class BannerSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Banner
        fields = ['id','link','image_url']


# 顶部/底部 导航
class NavSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Nav
        fields = ['id','title','link','is_site']