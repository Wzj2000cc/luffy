from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from . import models
from luffyapi.settings import contants

# 登录判断账号是否存在
def get_user_by_account(username):
    try:
        user = models.User.objects.get(Q(username=username) | Q(mobile=username))

    except models.User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):

    # todo 自定制登录认证功能
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password):
            return user


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username,
        'credit_to_money':contants.CREDIT_MONEY,
        'user_credit': user.credit
    }


def get_user_by_email(email):
    """
    用于验证邮箱是否存在
    """
    try:
        user = models.User.objects.get(email=email)
    except models.User.DoesNotExist:
        return None
    else:
        return user