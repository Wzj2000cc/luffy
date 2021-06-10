from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet
from .paginations import CustomPageNumberPagination


# Create your views here.

# 课程列表
class CourseCategoryAPIView(ListAPIView):
    queryset = models.CourseCategory.objects.filter(is_show=True, is_deleted=False).order_by('orders')
    serializer_class = serializers.CourseCategoryModelSerializer


# 课程章节课时展示
class CourseListAPIView(ListAPIView):
    queryset = models.Course.objects.filter(is_show=True, is_deleted=False).order_by('orders')
    serializer_class = serializers.CourseModelSerializer

    # 课程筛选
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filter_fields = ['course_category',]
    ordering_fields = ['id','students','price']
    pagination_class = CustomPageNumberPagination


class CourseDetailAPIView(RetrieveAPIView):
    queryset = models.Course.objects.filter(is_show=True, is_deleted=False).order_by('orders')
    serializer_class = serializers.CourseDetailSerializer




