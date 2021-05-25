from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

urlpatterns = [
    path(r'banner/',views.BannerAPIView.as_view()),
    path(r'nav/',views.HeaderNavAPIView.as_view()),
    path(r'btmnav/',views.BottomHeaderNavAPIView.as_view()),
]