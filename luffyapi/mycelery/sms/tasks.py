from mycelery.main import app
from luffyapi.libs.rly.SendMessage import send_message
from luffyapi.settings import contants
import logging

logger = logging.getLogger('django')

@app.task # 将这个函数指定成一个任务
def send_sms1(mobile,sms_code):
    """"""
    """
    请求容联云发送短信的任务
    调用SendMessage模块的方法将请求发送到容联云后端将随机验证码发送给该手机号
    """
    res = send_message(mobile,(sms_code,contants.SMS_EXPIRE_TIME//60),'1')
    if res.get('statusCode') != '000000':
        logger.error(f'{mobile}短信发送失败')

    return 'send sms task1'


@app.task  # 将这个函数指定成一个任务
def send_sms2():
    """
    发送短信的任务2
    """

    return 'send sms task2'