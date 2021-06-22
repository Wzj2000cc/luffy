from django.db import models
from luffyapi.utils.models import BaseModel
# Create your models here.

class Banner(BaseModel):
    """
    轮播广告图模型
    """
    title = models.CharField(max_length=500,verbose_name='广告标题')
    link = models.CharField(max_length=500,verbose_name='广告链接') # 点击跳转到指定页面

    image_url = models.ImageField(upload_to='banner',null=True,blank=True,max_length=255,verbose_name='广告图片')
    # upload_to: 设置上传文件的保存的子目录，将来上传文件时会保存到media下的banner文件夹下，这个字段本身存储图片地址
    # uploads/banner/图片.png
    # 一般情况下图片资源我们只是存储路径(若图片较小，会将数据存到数据库)

    remark = models.TextField(verbose_name='备注信息')

    # 轮播图会实时更新更换，加一个状态，控制轮播图是否显示
    is_show = models.BooleanField(default=False,verbose_name='是否显示')

    # 做一个排序功能，数字越大，越优先显示在前面
    orders = models.IntegerField(default=1,verbose_name='排序')

    # 假删除，删除数据就会标注为False
    is_deleted = models.BooleanField(default=False,verbose_name='是否删除')

    class Meta:
        db_table = 'ly_banner'
        verbose_name = '轮播广告'
        verbose_name_plural = verbose_name # 复数

    def __str__(self):
        return self.title


class Nav(BaseModel):
    """
    导航菜单模型
    """
    POSITION_OPTION = (
        (1,'顶部导航'),
        (2,'底部导航')
    )
    title = models.CharField(max_length=500,verbose_name='导航标题')
    link = models.CharField(max_length=500,verbose_name='导航链接')
    # 通过is_site判断是生成router-link标签（内链）还是a标签（外链）
    is_site = models.BooleanField(default=False,verbose_name='是否是站外链接')
    position = models.IntegerField(choices=POSITION_OPTION,default=1,verbose_name='导航位置')

    class Meta:
        db_table = 'ly_nav'
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title





