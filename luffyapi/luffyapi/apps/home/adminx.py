import xadmin
from xadmin import views
from . import models
from .models import Nav

class BaseSetting(object):
    '''xadmin的基本配置'''
    enable_themes = True #开启主题切换功能
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)

class GlobalSettings(object):
    '''admin的全局配置'''
    site_title = '路飞学城' #设置站点标题
    site_footer = '路飞学成有限公司' #设置站点的页脚
    # menu_style = 'accordion' #设置菜单折叠

xadmin.site.register(views.CommAdminView,GlobalSettings)

class BannerModelAdmin:
    list_display = ['title','orders','is_show']

xadmin.site.register(models.Banner,BannerModelAdmin)


class NavModelAdmin:
    list_display = ['id','title','link','is_site','is_show','is_deleted','position']

xadmin.site.register(Nav,NavModelAdmin)