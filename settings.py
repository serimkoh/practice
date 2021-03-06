"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mnwbrx3a5(+pwjx3!t=&wxn02ue6@9bzvkpx%+^qzb1be$jgut'
# 시크릿키는 csrf토큰을 만들때 사용되는 시드(종자값, 소금, 양념)
# 이 값을 어떻게 주느냐에 따라서 발급되는 값들이 천차만별임
# 시크릿 키는 절대 노출되면 안됨!!!!!!!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'firstapp',
    'secondapp',
    'thirdapp',
    'member',
    'paging',
    'file',
    'boardapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # 미들웨어라는 녀석이 우리 눈에 보이지 않게 어디선가 동작하고 있음
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'custom': { # thirdapp에서 사용할 데이터베이스 설정 추가
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'aivle',
    'USER': 'aivle',
    'PASSWORD': '1234',
    'HOST': '15.164.153.191',
    'PORT': 3306
    },
    'mini': { # miniproject에서 사용할 데이터베이스 설정 추가
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'aivle',
    'USER': 'root',
    'PASSWORD': 'aivle',
    'HOST': '34.64.201.231',
    'PORT': 3306
    }
    # 'serim': { # thirdapp에서 사용할 데이터베이스 설정 추가
    # 'ENGINE': 'django.db.backends.mysql',
    # 'NAME ': 'aivle_db',
    # 'USER': 'root',
    # 'PASSWORD': 'aivle053!',
    # 'HOST': '34.64.229.228',
    # 'PORT': 3306
    #  }
}
DATABASE_ROUTERS = ['thirdapp.router.DBRouter', 'boardapp.router.DBRouter']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers':{
        'console':
        {
            'level': 'DEBUG',
            'class':
            'logging.StreamHandler',
        }
    },
    'loggers':
    {'django.db.backends':
        {
            'handlers':
            ['console'],
            'level': 'DEBUG',
        },
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

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/member/login/'
LOGOUT_REDIRECT_URL = '/member/login/'

# MEDIA
MEDIA_URL = '/media/'
# 2.2버전
MEDIA_ROOT = os.path.join(BASE_DIR ,'media')
