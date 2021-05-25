from django.db import models

class BaseModel(models.Model):
    """ 公共模型 """
    # 轮播图会实时更新更换，加一个状态，控制轮播图是否显示
    is_show = models.BooleanField(default=False,verbose_name='是否显示')

    # 做一个排序功能，数字越大，越优先显示在前面
    orders = models.IntegerField(default=1,verbose_name='排序')

    # 假删除，删除数据就会标注为False
    is_deleted = models.BooleanField(default=False,verbose_name='是否删除')

    created_time = models.DateTimeField(auto_now_add=True,verbose_name='添加数据的时间')
    updated_time = models.DateTimeField(auto_now=True,verbose_name='修改数据的时间')

    class Meta:
        # 设置当前模型为抽象模型，数据库生成时不会生成该表
        abstract = True





