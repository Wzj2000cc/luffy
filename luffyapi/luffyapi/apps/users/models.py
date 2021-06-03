from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    mobile = models.CharField(max_length=12,verbose_name='手机号码')
    avatar = models.ImageField(upload_to='avatar',verbose_name='用户头像',null=True,blank=True)
    Wechat = models.CharField(max_length=50,null=True,blank=True,verbose_name='微信号')
    education = models.CharField(max_length=10,null=True,blank=True,verbose_name='学历')
    sex = models.CharField(max_length=5,null=True,blank=True,verbose_name='性别')
    birthday = models.CharField(max_length=20,null=True,blank=True,verbose_name='生日')
    address = models.CharField(max_length=50,null=True,blank=True,verbose_name='收件地址')
    autograph = models.CharField(max_length=100,null=True,blank=True,verbose_name='个性签名')

    class Meta:
        db_table = 'ly_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username