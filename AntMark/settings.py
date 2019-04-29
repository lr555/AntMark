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

CUR_HOST = 'http://127.0.0.1:8000/'

ALLOWED_HOSTS = ['localhost', '127.0.0.1','*']

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
    'DjangoUeditor',

    #my app
    'home',
    'users',
    'admin_manage',
    'commodity',
    'chatroom',
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
        'DIRS': [os.path.join(BASE_DIR, 'home','templates','home')],
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
MEDIA_DIRS = (
    os.path.join(BASE_DIR, 'media'),
)

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
