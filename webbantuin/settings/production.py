"""
Django settings for webbantuin project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# email
from django.core.mail import send_mail

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# kalau untuk local.py bagian ini bisa dihapus atau enggak juga gpp
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*72144ithyvwpu5z&h(=^dkyc9o_@mt=vsi8x2%m6%drp^2dqr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'home',
    'about',
    'profil',
]

# crispy template pack
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# jet admin template pack
JET_DEFAULT_THEME = 'default'

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    },
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

ROOT_URLCONF = 'webbantuin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'webbantuin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# di local.py pakai database yg ini
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# di production.py pakai database yg ini
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'afas',
        'USER': 'asd',
        'PASSWORD': 'dasca',
        'HOST': 'asdas',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    'static/'
)

# masa berlaku link aktivasi dari registrasi
ACCOUNT_ACTIVATION_DAYS = 7

# email backend django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# kalau punya akun mailtrap.io silahkan ganti host user dan host passwordnya dengan pengaturan di mailtrap kalian
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
# kalau mau ngetes di lokal saran saya pakai mailtrap jadi hapus tanda komentar biar bisa pakai mailtrap
# EMAIL_PORT = 2525
# EMAIL_HOST = 'mailtrap.io'
# EMAIL_HOST_USER = 'user'
# EMAIL_HOST_PASSWORD = 'pass'
# kalau mau ngetes pakai email gmail hapus tanda komentar biar bisa pakai gmail
EMAIL_PORT = 465
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'asdasd@zoho.com'
EMAIL_HOST_PASSWORD = 'asdasd' #change this
# SERVER_EMAIL = 'muhamadmashudiardiwinata@gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# login redirect after user login
LOGIN_REDIRECT_URL = '/'
