from django.urls import path,re_path
from . import views

urlpatterns = [
    path(r'category/', views.CourseCategoryAPIView.as_view()),
    path(r'list/', views.CourseListAPIView.as_view()),

    # 保利威接口
    path(r"player/", views.PolyvAPIView.as_view()),

    re_path(r'detail/(?P<pk>\d+)/$', views.CourseDetailAPIView.as_view()),
]