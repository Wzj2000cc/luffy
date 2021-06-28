from django.shortcuts import render
from . import models
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from . import models,serializers


# Create your views here.

class UserCouponAPIView(ListAPIView):
    # queryset = models.UserCoupon.objects.filter(is_show=True,
    #                                             is_deleted=False,
    #                                             is_use=False,
    #                                             user_id = )
    permission_classes = [IsAuthenticated, ]
    serializer_class = serializers.UserCouponModelSerializer

    # 重新定义get_queryset方法
    def get_queryset(self):
        return models.UserCoupon.objects.filter(is_show=True,
                                                is_deleted=False,
                                                is_use=False,
                                                user_id=self.request.user.id)
