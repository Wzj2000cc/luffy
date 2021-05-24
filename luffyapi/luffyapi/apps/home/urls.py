from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

urlpatterns = [
    path(r'banner/',views.BannerAPIView.as_view()),
]