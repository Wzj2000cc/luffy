"""
Django settings for luffyapi project.

Generated by 'django-admin startproject' using Django 2.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os,sys,datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't5c(=51h9yg6mdjxfy*ru3&4yovvfvl%lyo!ixfn--gvviy(5k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api.luffycity.cn',
                 'www.luffycity.cn',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    # 配置xadmin应用
    'xadmin',
    'crispy_forms',
    'reversion',
    'django_filters',
    'ckeditor', # 富文本编辑器
    'ckeditor_uploader', # 富文本编辑器上传图片

    'home', # 飘黄，因为没在sys.path里面,上面已经配置
    'users',
    'course',
    'cart',
    'order',
    'coupon',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'luffyapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'luffyapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'luffy', # 要连接的数据库，连接前需要创建好
        'USER':'luffy_user',# 连接数据库的用户名
        'PASSWORD':'luffy', # 连接数据库的密码
        'HOST':'127.0.0.1',       # 连接主机，默认本级
        'PORT':3306, #  端口 默认3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = True

USE_TZ = False

# APPEND_SLASH = True

# 配置自定义用户模型
AUTH_USER_MODEL = 'users.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 上传的文件，图片都会保存到media文件夹下
MEDIA_ROOT = os.path.join(BASE_DIR,'uploads')
MEDIA_URL = '/media/' # 路径别名

REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER':'luffyapi.utils.exceptions.custom_exception_handler',

    'DEFAULT_AUTHENTICATION_CLASSES':(
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication'),
}


# 日志配置
LOGGING = {
    'version': 1,  #使用的python内置的logging模块，那么python可能会对它进行升级，所以需要写一个版本号，目前就是1版本
    'disable_existing_loggers': False, #是否去掉目前项目中其他地方中以及使用的日志功能，但是将来我们可能会引入第三方的模块，里面可能内置了日志功能，所以尽量不要关闭。
    'formatters': { #日志记录格式
        'verbose': { #levelname等级，asctime记录时间，module表示日志发生的文件名称，lineno行号，message错误信息
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': { #过滤器：可以对日志进行输出时的过滤用的
        # 这两个是固定的写法。
        'require_debug_true': { # 在debug=True下产生的一些日志信息，要不要记录日志，需要的话就在handlers中加上这个过滤器，不需要就不加
            '()': 'django.utils.log.RequireDebugTrue',
        },
        """
        debug: True，Django里面有一个这个配置，开发测试模式下 访问系统出错的时候，会出现大黄页。
        线上时我们改成False。
        """
        'require_debug_false': { #和上面相反
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    # 日志实例，这里面没有做发送邮件的
    'handlers': { #日志处理方式，日志实例
        'console': { #在控制台输出时的实例
            'level': 'DEBUG', #日志等级；debug是最低等级，那么只要比它高等级的信息都会被记录
            'filters': ['require_debug_true'], #在debug=True下才会打印在控制台
            'class': 'logging.StreamHandler', #使用的python的logging模块中的StreamHandler来进行输出
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/luffy.log"), #注意，你的文件应该有读写权限。
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
    },
    # 日志对象
    'loggers': {
        'django': {  #和django结合起来使用，将django中之前的日志输出内容的时候，按照我们的日志配置进行输出，
            'handlers': ['console', 'file'], #将来项目上线，把console去掉
            'propagate': True, #冒泡：是否将日志信息记录冒泡给其他的日志处理系统，工作中都是True，不然django这个日志系统捕获到日志信息之后，其他模块中可能也有日志记录功能的模块，就获取不到这个日志信息了
        },
    }
}

# 请求白名单
CORS_ORIGIN_WHITELIST = [
    'http://www.luffycity.cn:8080',
]
CORS_ALLOW_CREDENTTALS = False

# 登录时客户端保存JWT信息
JWT_AUTH={
    # 设置过期时间
    'JWT_EXPIRATION_DELTA':datetime.timedelta(days=7),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',
}

# 配置自定义认证
AUTHENTICATION_BACKENDS = [
    'users.utils.UsernameMobileAuthBackend'
]

# Redis数据库配置
CACHES = {
    # 默认缓存
    "default": {
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 也可以指定缓存的库 session存储配置刀redis里面去，不用的功能在不同的库。
    # 通过select 1 可以奇幻库
    # 提供给xadmin或者admin的session存储
    "session": {
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "sms_code": {
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "cart": {
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

# 设置xadmin用户登录时，登录信息session保存到redis
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


# 容联云配置
SMS = {
    'accId' : '8aaf070879c5511c0179c677556200d7',   # 容联云通讯分配的主账号ID
    'accToken' : '6336a73584a0413b8ed3053ebceaf30c',  # 容联云通讯分配的主账号TOKEN
    'appId' : '8a216da879c0854b0179c679d3ab0248' # 容联云通讯分配的应用ID
}


#邮箱验证
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True # 是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = True # 是否使用SSL加密，qq企业邮箱要求使用
# EMAIL_USE_SSL = False #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.qq.com'
# 发送邮件的邮箱 的 SMTP服务器,固定格式,如果是其他的邮箱则是'smtp.xx.com'
# EMAIL_PORT = 25     # 发件箱的SMTP服务器端口,默认
EMAIL_PORT = 465     # 发件箱的SMTP服务器端口,默认
EMAIL_HOST_USER = '2530065079@qq.com'    # 发送邮件的邮箱地址,
EMAIL_HOST_PASSWORD = 'ehwesfqxqppkdhha'


# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar':'full',
        'height':300,    # 文本框高度
        # 'width':
    },
}
CKEDITOR_UPLOAD_PATH = ''