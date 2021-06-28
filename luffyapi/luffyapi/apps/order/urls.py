from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

# patch用于局部数据修改，put用于全部数据修改
urlpatterns = [
    path(r'',views.OrderAPIView.as_view()),
]