from django.shortcuts import render
from rest_framework.generics import ListAPIView

from . import models
from . import serializers

# Create your views here.

class CourseCategoryAPIView(ListAPIView):
    queryset = models.CourseCategory.objects.filter(is_show=True, is_deleted=False).order_by('orders')
    serializer_class = serializers.CourseCategoryModelSerializer

