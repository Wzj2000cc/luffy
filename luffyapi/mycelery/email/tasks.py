from mycelery.main import app
from celery.schedules import crontab
import requests

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

@app.task(name='email') # name='email'：起别名
def send_email():
    """
    celery定时爬取
    """
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    for page in range(1,6):
        data={
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        response=requests.post(url=url,headers=headers,data=data).json()

        for i in response['list']:

            url1='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
            data1={
                'id':i['ID']
            }
            response1=requests.post(url=url1,data=data1,headers=headers).json()
            return response1

app.conf.beat_schedule = {
    'send_everyday_pm_3:30': {
        'task': 'email.tasks',
        'schedule': crontab(minute='50', hour='8'),
        'args': ()
    }
}

app.conf.enable_utc = False
app.conf.timezone = 'Asia/Shanghai'