from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderModelSerializer


# Create your views here.

class OrderAPIView(CreateAPIView):
    """订单视图接口"""
    queryset = Order.objects.filter(is_deleted=False, is_show=True)
    serializer_class = OrderModelSerializer
    permission_classes = [IsAuthenticated,]







