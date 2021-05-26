from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path(r'login/',obtain_jwt_token),
]