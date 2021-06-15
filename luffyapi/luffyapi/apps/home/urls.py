from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

urlpatterns = [
    # 轮播图
    path(r'banner/',views.BannerAPIView.as_view()),
    # 导航栏顶部
    path(r'nav/',views.HeaderNavAPIView.as_view()),
    # 底部导航栏
    path(r'btmnav/',views.BottomHeaderNavAPIView.as_view()),
]