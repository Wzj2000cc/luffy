"""luffyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.views.static import serve
import xadmin
from xadmin.plugins import xversion




urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    # serve 将来上传的文件，图片会通过serve处理保存到相应的uploads目录下
    re_path(r'media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    # 轮播图应用
    path(r'home/',include('home.urls')),
    # 登录，注册应用
    path(r'users/',include('users.urls')),
    # 课程详情页面
    path(r'course/',include('course.urls')),

]
