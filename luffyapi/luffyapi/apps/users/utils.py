from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from . import models

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