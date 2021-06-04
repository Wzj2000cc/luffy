from django.urls import path
from . import views

urlpatterns = [
    path(r'category/', views.CourseCategoryAPIView.as_view()),
    path(r'list/', views.CourseListAPIView.as_view()),
]