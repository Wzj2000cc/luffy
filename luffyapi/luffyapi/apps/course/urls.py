from django.urls import path
from . import views

urlpatterns = [
    path(r'category/', views.CourseCategoryAPIView.as_view()),
]