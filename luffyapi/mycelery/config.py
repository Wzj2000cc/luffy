from __future__ import absolute_import
# 任务队列的链接地址（变量名不能改变）
broker_url = "redis://127.0.0.1:6379/14"

# 结果队列的链接地址(变量名不能变)
result_backend = "redis://127.0.0.1:6379/15"

from celery.schedules import crontab
from .main import app
from luffyapi.settings import dev
# 定时任务的调度列表，用于注册定时任务
app.conf.timezone = dev.TIME_ZONE
app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'check_order_outtime': {
        # 本次调度的任务
        'task': 'check_o', # 这里的任务名称必须先到main.py中注册
        # 上面要使用别名 如果没有使用别名只能使用路径 mycelery.order.tasks.check_order

        # 定时任务的调度周期
        # 'schedule': crontab(minute=0, hour=0),   # 每周凌晨00:00
        'schedule': crontab(),   # 每分钟 每分钟的零秒执行
        # 'args': (16, 16),  # 注意：任务就是一个函数，所以如果有参数则需要传递
    },
}