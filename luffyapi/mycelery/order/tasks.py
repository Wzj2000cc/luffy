# from mycelery.main import app
# from order.models import Order
# from luffyapi.settings.contants import ORDER_TIMEOUT
# from datetime import datetime
#
# @app.task(name='check_o')
# def check_order():
#     print('123123')
#     """定时查看所有的订单，只要有超时的未支付的订单，将其order_status=3"""
#     now_time = datetime.now().timestamp()
#     timeout_number = now_time - ORDER_TIMEOUT
#     timeout = datetime.fromtimestamp(timeout_number)
#     timeout_order_list = Order.objects.filter(order_status=0, created_time__lt=timeout)
#     for order in timeout_order_list:
#         order.order_status = 3
#         order.save()
#     return now_time


from mycelery.main import app
from order.models import Order
from luffyapi.settings.contants import ORDER_TIMEOUT
from datetime import datetime

@app.task(name='check_o')
def check_order():
    print('123123')
    """定时查看所有的订单，只要有超时的未支付的订单，将其order_status=3"""
    now_time = datetime.now().timestamp()
    timeout_number = now_time - ORDER_TIMEOUT
    timeout = datetime.fromtimestamp(timeout_number)
    timeout_order_list = Order.objects.filter(order_status=0, created_time__lt=timeout)
    for order in timeout_order_list:
        order.order_status = 3
        order.save()