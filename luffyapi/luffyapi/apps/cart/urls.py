from cart import views
from rest_framework.routers import DefaultRouter
from django.urls import path

# patch用于局部数据修改，put用于全部数据修改
urlpatterns = [
    path(r'',views.CartAPIView.as_view({
        'post':'add','get':'cart_list',
        'patch':'change_course_selected',
        'put':'change_expire',
        'delete': 'delete_course',
         })),
]