from celery import Celery
import os,django

os.environ.setdefault('FORKED_BY_MULTIPROCESSING','1')

# todo 引入django项目的环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
django.setup()

# 1. 创建celery对象实例（可以创建多个应用）
app = Celery('luffy')
# app02 = Celery('luffy_shop')

# 2. 加载配置（给应用对象指定任务队列及结果队列）
app.config_from_object('mycelery.config')

# 3. 自动发信任务
app.autodiscover_tasks(['mycelery.order',])