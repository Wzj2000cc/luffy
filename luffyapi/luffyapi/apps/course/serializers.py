from rest_framework import serializers
from . import models


class CourseCategoryModelSerializer(serializers.ModelSerializer):
    """ 展示课程列表的序列化器"""
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']
