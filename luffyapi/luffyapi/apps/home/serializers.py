from rest_framework import serializers
from . import models

class BannerSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Banner
        fields = ['id','link','image_url']