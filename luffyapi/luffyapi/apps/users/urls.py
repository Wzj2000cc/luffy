from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    # 登录JWT认证
    path(r'login/',obtain_jwt_token),
    # 登录极速验证滑动验证；
    path(r'capycha/', views.GeetestView.as_view()),
    # 注册
    path(r'register/', views.UserAPIView.as_view()),

    # 个人订单页面
    path(r'order/', views.UserOrderAPIView.as_view()),
    # 个人资料
    re_path(r'account/(?P<pk>\d+)',views.AccountAPIView.as_view({'get':'retrieve','put':'update'})),

    # 注册页面校验手机号是否已经存在
    re_path(r'mobile/(?P<mobile>1[3-9]\d{9})/$', views.MobileAPIView.as_view()),
    # 注册容联云手机号验证
    re_path(r'sms/(?P<mobile>1[3-9]\d{9})/$', views.SMSAPIView.as_view()),

    # 点击忘记密码发送qq邮箱
    re_path(r'mailbox/(?P<email>.*)/$', views.Mailbox.as_view()),
    # 修改密码
    re_path(r'password/(?P<pk>\d+)/', views.PasswordAPIView.as_view()),
]