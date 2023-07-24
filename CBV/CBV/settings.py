"""
Django settings for CBV project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z+6j7v8ye()jde_uv6ah6oiwv28^%b4(+jc7z6krneb(_6+yaq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'simpleui', # admin界面美化，必须写在 .admin 之上 pip install django-simpleui
    'django.contrib.admin', # django 内置的admin
    'django.contrib.auth',  # 系统认证
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',     # 登录鉴权
    'rest_framework.authtoken',     # Token验证
    'corsheaders',  # 跨域支持
    'user',
    'drfdemo',
    'app01',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',    # 跨域资源共享中间件，设置务必位于 .CommonMiddleware 之上
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',    # 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CBV.urls'

# 跨域请求
CORS_ORIGIN_ALLOW_ALL = True    # 允许任意客户端发送请求访问当前服务端
# CORS_ORIGIN_WHITELIST = [     # 允许访问的客户端白名单
    # "http://localhost:3000",
    # ]    


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

WSGI_APPLICATION = 'CBV.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 指定自定义用户类
AUTH_USER_MODEL = 'drfdemo.User'

# DRF 配置
REST_FRAMEWORK = {
    # 登录鉴权方式
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',     # 基本认证方式
        'rest_framework.authentication.SessionAuthentication',   # session认证
        #添加Token验证，若是Token过时，不须要登陆的界面也不能访问，最好配置在具体的页面
        # 'rest_framework.authentication.TokenAuthentication',     
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 默认全局权限配置
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAdminUser',   # 只允许管理员用户访问
        'rest_framework.permissions.IsAuthenticated', # 已经登录认证的用户才能访问
        # 'rest_framework.permissions.AllowAny',      # 允许所有用户进行所有操作
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',   # 允许认证用户完全操作，未认证用户只能GET读取
    ),
    # 'EXCEPTION_HANDLER': 'common.exceptions.except_handler',
}

# Token 相关配置
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),      # 访问令牌的有效时间
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),        # 刷新令牌的有效时间
    
    "ROTATE_REFRESH_TOKENS": False,       # 若为True，则刷新后新的refresh_token有更新的有效时间
    "BLACKLIST_AFTER_ROTATION": True,     # 若为True，则刷新后的token将添加到黑名单中
    "UPDATE_LAST_LOGIN": False,
    
    "ALGORITHM": "HS256",       # 对称算法：HS256 HS384 HS512  非对称算法： RSA
    "SIGNING_KEY": "SECRET_KEY",  # if signing_key,verifying_key will be ignore.
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    'JWK_URL': None,
    'LEEWAY': 0,
    
    "AUTH_HEADER_TYPES": ("Bearer",),   # Authorization: Bearer <token>
    "Auth_HEADER_NAME": "HTTP_AUTHORIZATION",   # if HTTP_X_ACCESS_TOKEN, X_ACCESS_TOKEN: Bearer <token>
    "USER_ID_FIELD": "id",              # 使用唯一不变的数据库字段，将包含在生成的令牌中用以标识用户
    "USER_ID_CLAIM": "user_id",
    # "USER_AUTHENTICATION_RULE": 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    # "AUTH_TOKEN_CLASSES": ('rest_framework_simplejwt.tokens.AccessToken',),
    # "TOKEN_TYPE_CLAIM": 'token_type',
    # 'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
    
    # 'JTI_CLAIM': 'jti',
    
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# jwt设置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(days=1),  # 设置 JWT Token 的有效时间
    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # 设置 请求头中的前缀，不写默认是"JWT "
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.jwt_handler.jwt_response_payload_handler',
}


# 配置自定义多字段用户登录验证
AUTHENTICATION_BACKENDS = [
    'common.authenticate.MyBackends',
]

# 设置 media 用户目录, 上传文件保存路径
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_ROOT = BASE_DIR / 'media' 
MEDIA_URL = "media/"