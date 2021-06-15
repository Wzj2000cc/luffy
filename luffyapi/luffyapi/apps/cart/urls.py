from cart import views
from rest_framework.routers import DefaultRouter
from django.urls import path

urlpatterns = [
    path(r'',views.CartAPIView.as_view({'post':'add','get':'cart_list'})),
]