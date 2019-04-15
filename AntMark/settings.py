"""
Django settings for AntMark project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, socket
from datetime import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wpcq2fia!%f@5w_7c@n(%(3s!1ks$=&*_w4n#n5mskvjaw__jj'

# SECURITY WARNING: don't run with debug turned on in production!
# if socket.gethostbyname(socket.gethostname())[:3]=='192':
#     DEBUG = TEMPLATE_DEBUG = True
# else:
#     DEBUG = TEMPLATE_DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'schnee.pro', '*.schnee.pro']

ADMINS = (
    ('suzh', '1194133793@qq.com')
)

SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS
 

EMAIL_HOST = "smtp.sina.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "antmark_mail@sina.com"         # 你的邮箱账号
EMAIL_HOST_PASSWORD = "AntMarkAdmin2019"          # 你的邮箱密码
EMAIL_USE_TLS = False                             # 这里是 False
EMAIL_FROM = "antmark_mail@sina.com"              # 你的邮箱账号
DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER


#logging日志配置
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {                                         #日志格式 
#        'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'} 
#     },
#     'filters': {                                            #过滤器
#         'require_debug_false': {
#                 '()': 'django.utils.log.RequireDebugFalse',
#             }
#     },
#     'handlers': {                                           #处理器
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'mail_admins': {                                    #发送邮件通知管理员
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false'],             # 仅当 DEBUG = False 时才发送邮件
#             'include_html': True,
#         },
#         'debug': {                                          #记录到日志文件(需要创建对应的目录，否则会出错)
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, "log",'debug.log'),      #日志输出文件
#             'maxBytes':1024*1024*5,                                     #文件大小 
#             'backupCount': 5,                                           #备份份数
#             'formatter':'standard',                                     #使用哪种formatters日志格式
#         },
#         'console':{                                         #输出到控制台
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard',
#         },
#     },
#     'loggers': {                                            #logging管理器
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False 
#         },
#         'django.request': {
#             'handlers': ['debug','mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
#         'django.security.DisallowedHost': {
#             'handlers': ['null'],
#             'propagate': False,
#         },
#     } 
# }

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third party app
    'bootstrap4',
    'widget_tweaks',

    #my app
    'home',
    'users',
    'commodity',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AntMark.urls'

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
            
            'libraries':{
                "base":"home.templatetags.base",
            },
        },
    },
]

WSGI_APPLICATION = 'AntMark.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "commodity", "static"),
]


# upload folder
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SIMDITOR_UPLOAD_PATH = '/media/uploads/'
SIMDITOR_IMAGE_BACKEND = 'pillow'

SIMDITOR_TOOLBAR = [
    'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale',
    'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link',
    'image', 'hr', '|', 'indent', 'outdent', 'alignment', 'fullscreen',
    'markdown', 'emoji'
]

SIMDITOR_CONFIGS = {
    'toolbar': SIMDITOR_TOOLBAR,
    'upload': {
        'url': '/simditor/upload/',
        'fileKey': 'upload',
        'image_size': 1024 * 1024 * 4   # max image size 4MB
    },
    'emoji': {
        'imagePath': '/static/simditor/images/emoji/'
    }
}

# markdownx options
MARKDOWNX_EDITOR_RESIZABLE = False
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.codehilite',
]
MARKDOWNX_MEDIA_PATH = datetime.now().strftime('markdown/upload/%Y/%m/%d')
MARKDOWNX_UPLOAD_MAX_SIZE = 4 * 1024 * 1024
MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/svg+xml']
MARKDOWNX_IMAGE_MAX_SIZE = {
    'size': (800, 500),
    'quality': 90
}

LOGIN_URL = '/users/login'

BOOTSTRAP4 = {
    'include_jquery': True,
}

CUR_HOST = 'http://127.0.0.1:8000/'