from mycelery.main import app

@app.task(name='email') # name='email'：起别名
def send_email():
    """
    发送邮箱任务
    :return:
    """
    return 'send email task'