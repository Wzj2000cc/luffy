from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .geetest import GeetestLib
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from . import models
from .serializers import UserModelSerializer
from .utils import get_user_by_account

# Create your views here.


# todo 实现验证码功能的接口类
class GeetestView(APIView):

    captcha_id = "5e876edb2bda195c265416b70e7389a7"
    private_key = "c1f0f6f5958507924d187db31cd136e5"
    user_id ='test'
    status = 1  # 0或1 如果是1代表第一次验证成功

    # 给前端获取验证码
    def get(self,request):

        gt = GeetestLib(self.captcha_id,self.private_key)
        status = gt.pre_process(self.user_id) # status=0或1
        # request.session[gt.GT_STATUS_SESSIONKEY] = status
        # request.session["user_id"] = user_id
        response_str = gt.get_response_str()
        return HttpResponse(response_str)


    def post(self, request):
        gt = GeetestLib(self.captcha_id, self.private_key)
        challenge = request.data.get(gt.FN_CHALLENGE, '')
        validate = request.data.get(gt.FN_VALIDATE, '')
        seccode = request.data.get(gt.FN_SECCODE, '')
        # status = request.session[gt.GT_STATUS_SESSION_KEY]
        # user_id = request.session["user_id"]
        if self.status:
            result = gt.success_validate(challenge, validate, seccode, self.user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = {"status":"success"} if result else {"status":"fail"}
        return Response(result)


# 注册用户信息
class UserAPIView(CreateAPIView):

    queryset = models.User.objects.all()
    serializer_class = UserModelSerializer


# todo 校验手机号是否存在的接口
class MobileAPIView(APIView):

    def get(self,request,mobile):
        print(mobile)
        user = get_user_by_account(mobile)
        print(user)
        if user is not None:
            return Response({"msg":"抱歉，该手机号已被注册"},status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg':'注册成功，手机号格式正确！'},status=status.HTTP_200_OK)



