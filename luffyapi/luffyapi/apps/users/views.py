import random,logging
import re

from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .geetest import GeetestLib
from django.shortcuts import render,HttpResponse
from django_redis import get_redis_connection
from luffyapi.settings import contants
from luffyapi.libs.rly.SendMessage import send_message

from luffyapi.settings import dev
from . import models
from .serializers import UserModelSerializer,AccountModelSerializer,UserRetrieveModelSerializer
from .utils import get_user_by_account, get_user_by_email


# Create your views here.
# 实例化日志对象
logger = logging.getLogger('django')

# todo 极速验证实现登录短信验证码功能的接口类
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
        result = {"status":"success"} if result else {"status":"faile"}
        return Response(result)


# 注册用户信息
class UserAPIView(ListCreateAPIView):

    queryset = models.User.objects.all()
    serializer_class = UserModelSerializer


# 个人资料
class AccountAPIView(ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = AccountModelSerializer


# 校验手机号是否存在的接口
class MobileAPIView(APIView):

    def get(self,request,mobile):
        user = get_user_by_account(mobile)
        print(user)
        if user is not None:
            return Response({"msg":"抱歉，该手机号已被注册"},status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg':'注册成功，手机号格式正确！'},status=status.HTTP_200_OK)


# todo 容联云实现注册获取短信验证码
class SMSAPIView(APIView):

    def get(self,request,mobile):

        redis_conn = get_redis_connection('sms_code')
        check_ret = redis_conn.get(f'mobile_{mobile}')
        if check_ret:
            return Response({'msg':'60秒内不能重复发送'})

        try:
            # 1. 随机生成6位验证码
            sms_code = '%06d' % random.randint(0,999999)

            # 2. 将随机验证码保存到redis数据库里

            # 创建redis管道
            pipe = redis_conn.pipeline()
            # 开启管道
            pipe.multi()

            pipe.setex(f'sms_{mobile}',contants.SMS_EXPIRE_TIME,sms_code)

            # 3. 设置一个时间间隔的键值对
            pipe.setex(f'mobile_{mobile}',contants.SMS_INTERVAL_TIME,'__')

            # 执行管道
            pipe.execute()

            # 4. 调用SendMessage模块的方法将请求发送到容联云后端将随机验证码发送给该手机号
            # res = send_message(mobile,(sms_code,contants.SMS_EXPIRE_TIME//60),'1')
            # if res.get('statusCode') == '000000':
            #     return Response({'msg':'短信发送成功'},status=status.HTTP_200_OK)
            # logger.error(f'{mobile}短信发送失败')
            # return Response({'msg':'短信发送失败'},status=status.HTTP_400_BAD_REQUEST

            """
            4. 通过celery异步处理请求容联云服务端，主线程不受子线程IO影响
            """
            from mycelery.sms.tasks import send_sms1
            send_sms1.delay(mobile,sms_code)
            return Response({'msg':'手机验证码已发送，请注意查收'})

        except:
            logger.error('服务器内部错误')
            return Response({'msg':'服务器内部错误'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# todo 忘记密码发送qq邮箱
class Mailbox(APIView):
    redis_conn = get_redis_connection('sms_code')

    # get获取验证码邮件
    def get(self, request, email):
        if re.match(r'^.*@.*[.].*$', email):
            user = get_user_by_email(email)
            if user is not None:
                captcha = random.sample('zyxwvutsrqponmlkjihgfedcba1234567890123456789ABCDEFGHIGKLMNOPQRSGHIJKLMNOPQRSTUWXYZ', 6)
                captcha = ''.join(captcha)
                try:
                    print(captcha)
                    send_mail('欢迎使用路飞学成网页系统，验证码5分钟内有效，请及时查收', captcha, dev.EMAIL_HOST_USER, [email])
                    self.redis_conn.setex(f'sms_{email}', contants.SMS_EXPIRE_TIME, captcha)
                    return Response({'msg': '发送成功'}, status=status.HTTP_200_OK)
                except EOFError:
                    return Response({'msg': '发送失败'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg': '邮箱尚未注册'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': '邮箱格式不正确'}, status=status.HTTP_412_PRECONDITION_FAILED)

    # post提交前端验证码判断对否
    def post(self, request, email):
        try:
            code = request.data.get('email_code')
            redis_sms_code = self.redis_conn.get(f'sms_{email}').decode()
            if code == redis_sms_code:
                user_data = models.User.objects.get(email=email)
                return Response({'msg': '验证码正确', 'user_id': user_data.id, 'user_mobile': user_data.mobile},
                                status=status.HTTP_200_OK)
            return Response({'msg': '验证码不正确'}, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response({'msg': '输入信息有误'}, status=status.HTTP_400_BAD_REQUEST)


# 忘记密码修改密码
class PasswordAPIView(RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserRetrieveModelSerializer