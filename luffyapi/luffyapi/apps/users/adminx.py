import xadmin
from .models import Credit

class CreditModelAdmin(object):
    """订单模型管理类"""
    pass

xadmin.site.register(Credit, CreditModelAdmin)