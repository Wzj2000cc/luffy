import re

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from . import models
from .utils import get_user_by_account

from django.contrib.auth.hashers import make_password
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
        print(attrs)
        """
        全局钩子
        """
        mobile = attrs.get('mobile')
        sms_code = attrs.get('sms_code')

        if not re.match(r'^1[3-9]\d{9}$',mobile):
            raise serializers.ValidationError('手机号格式错误！')
        if get_user_by_account(mobile):
            raise serializers.ValidationError('该手机号已被注册过！')

        # todo：短信验证码是否正确
        return attrs

    def create(self, validated_data):
        """
        我们要注册用户
        1. 前端传来的密码需要加密
        2. 随机生成用户名
        :param validated_data:
        :return:
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