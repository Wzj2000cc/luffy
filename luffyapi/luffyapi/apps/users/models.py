from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    mobile = models.CharField(max_length=12,verbose_name='手机号码')
    avatar = models.ImageField(upload_to='avatar',verbose_name='用户头像',null=True,blank=True)
    Wechat = models.CharField(max_length=50,null=True,blank=True,verbose_name='微信号')

    class Meta:
        db_table = 'ly_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username