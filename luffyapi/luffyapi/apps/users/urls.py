from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserAPIView

urlpatterns = [
    path(r'login/',obtain_jwt_token),
    path(r'capycha/', views.GeetestView.as_view()),
    path(r'register/', UserAPIView.as_view()),
    re_path(r'mobile/(?P<mobile>1[3-9]\d{9})/$', views.MobileAPIView.as_view()),
]