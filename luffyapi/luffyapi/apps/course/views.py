from django.shortcuts import render,HttpResponse
from rest_framework.generics import ListAPIView,RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# 保利威引用
from luffyapi.libs.polyv import PolyvPlayer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.response import Response



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


class PolyvAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        """获取视频播放的token"""
        userId = settings.POLYV_CONFIG["userId"]
        secretkey = settings.POLYV_CONFIG["secretkey"]
        tokenUrl = settings.POLYV_CONFIG["tokenUrl"]
        polyv = PolyvPlayer(userId,secretkey,tokenUrl)

        vid = request.query_params.get("vid")
        # vid = '7617a871cec483f03a14d24f0c8f0275_7'
        viewerIp = request.META.get("REMOTE_ADDR")  # 用户的IP
        viewerId = request.user.id      # 用户ID
        # viewerId = 1      # 用户ID
        viewerName = request.user.username  # 用户名
        # viewerName = 'root'  # 用户名

        result = polyv.get_video_token(vid, viewerIp, viewerId,viewerName)
        # return Response(result)
        """
        {
            "token": "cae9bc15-302f-40f4-a54b-285b1349aeae-s1",
            "userId": "7617a871ce",
            "appId": null,
            "videoId": "7617a871cec483f03a14d24f0c8f0275_7",
            "viewerIp": "127.0.0.1",
            "viewerId": "1",
            "viewerName": "root",
            "extraParams": "HTML5",
            "ttl": 600000,
            "createdTime": 1625380116945,
            "expiredTime": 1625380716945,
            "iswxa": 0,
            "disposable": false
        }
        """
        return HttpResponse(result.get('token'))




