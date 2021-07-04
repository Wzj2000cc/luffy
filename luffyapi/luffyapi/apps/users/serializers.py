import re

from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from . import models
from .utils import get_user_by_account
from django.contrib.auth.hashers import make_password

from order.models import Order



# 注册功能序列化器反序列化
class UserModelSerializer(serializers.ModelSerializer):

    sms_code = serializers.CharField(min_length=4,max_length=6,required=True,help_text='短信验证码',write_only=True)
    token = serializers.CharField(max_length=1024,help_text='token密文',read_only=True)

    class Meta:
        model = models.User
        fields = ['mobile','password','sms_code','id','username','token']
        extra_kwargs = {
            "id":{"read_only":True},
            "username":{"read_only":True},
            "mobile":{'write_only':True},
            "password":{'write_only':True},
        }

    def validate(self, attrs):
        """
        全局钩子
        """
        mobile = attrs.get('mobile')
        sms_code = attrs.get('sms_code')

        if not re.match(r'^1[3-9]\d{9}$',mobile):
            raise serializers.ValidationError('手机号格式错误！')
        if get_user_by_account(mobile):
            raise serializers.ValidationError('该手机号已被注册过！')

        # todo：短信验证码是否正确(校验)
        redis_conn = get_redis_connection('sms_code')
        redis_sms_code = redis_conn.get(f'sms_{mobile}').decode()
        if sms_code != redis_sms_code:
            raise serializers.ValidationError('验证码输入有误')
        return attrs


    def create(self, validated_data):
        """
        我们要注册用户
        1. 前端传来的密码需要加密
        2. 随机生成用户名
        """
        mobile = validated_data.get('mobile')
        password = validated_data.get('password')

        # 新建的用户名唯一
        new_username = f'user_{mobile}'
        # 密文形式的密码
        hash_password = make_password(password)

        # 新信息写入数据库
        user = models.User.objects.create(
            mobile=mobile,
            password=hash_password,
            username=new_username,
        )

        # 自动生成JWT密文
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user


# 个人资料序列化器
class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


# qq邮箱找回密码序列化器
class UserRetrieveModelSerializer(serializers.ModelSerializer):

    # 表中没有的字段
    password2 = serializers.CharField(min_length=2, max_length=50, required=True, help_text='重复输入密码', write_only=True)
    token = serializers.CharField(max_length=1024, help_text='token认证字符串', read_only=True)

    class Meta:
        model = models.User
        fields = ['password','password2','token']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def validate(self, attrs):
        """全局钩子，判断两次输入密码是否相同"""
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('两次密码不正确')
        return attrs

    # put请求获取前端密码，修改数据库的密码
    def update(self, instance, validated_data):
        password = validated_data.get('password')
        user = instance
        hash_password = make_password(password)
        models.User.objects.filter(id=instance.id).update(password=hash_password)



class UserOrderModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['order_title', 'total_price', 'real_price', 'order_number', 'order_status', 'pay_type', 'credit',
                  'coupon', 'order_desc', 'created_time', 'user', 'order_course']