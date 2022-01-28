from pathlib import Path
from datetime import timedelta
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Heroku用
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-47$10)sj8p81rp*fy+8z88%9wn6xrxvzb+gov=s$%*s6xit(=_'


ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1:8000', 'localhost', '127.0.0.1', 'kasokomi.herokuapp.com']
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'channels',
    'djoser',
    'corsheaders',
    'accounts',
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

AUTH_USER_MODEL = 'accounts.UserAccount'

# ASGI_APPLICATION = "mysite.asgi.application"
WSGI_APPLICATION = 'mysite.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_FILES_DIRS = [os.path.join(BASE_DIR / 'static')]
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ローカル確認用
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 本番環境用
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# 詳しくは→[https://docs.djangoproject.com/en/4.0/ref/settings/]に記載されている
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kamotoshi.workingo@gmail.com'
EMAIL_HOST_PASSWORD = 'Syun!0514'
EMAIL_USE_TLS = True
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# DOMAIN = ('localhost:3000')
DOMAIN = ('kasokomi.herokuapp.com')
# SITE_NAME = ('YOUR_SITE_NAME')

REST_FRAMEWORK = {
    # 認証が必要
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # JWT認証
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # "rest_framework.authentication.TokenAuthentication",
    ],
    'DATETIME_FORMAT': '%m/%d %H:%M'
}

SIMPLE_JWT = {
    # アクセストークン(1時間)
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    # リフレッシュトークン(3日)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    # 認証タイプ
    'AUTH_HEADER_TYPES': ('JWT', ),
    # 認証トークン
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', )
}

DJOSER = {
    # メールアドレスでログイン
    'LOGIN_FIELD': 'email',
    # アカウント本登録メール
    'SEND_ACTIVATION_EMAIL': True,
    # アカウント本登録完了メール
    'SEND_CONFIRMATION_EMAIL': True,
    # メールアドレス変更完了メール
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    # パスワード変更完了メール
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # アカウント登録時に確認用パスワード必須
    'USER_CREATE_PASSWORD_RETYPE': True,
    # メールアドレス変更時に確認用メールアドレス必須
    'SET_USERNAME_RETYPE': True,
    # パスワード変更時に確認用パスワード必須
    'SET_PASSWORD_RETYPE': True,
    # 'USERNAME_RESET_CONFIRM_RETYPE': True,
    # 確認用メールがない場合は400エラーが出る
    # 'USERNAME_RESET_SHOW_EMAIL_NOT_FOUND': True,
    # アカウント本登録用URL
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    # メールアドレスリセット完了用URL
    'USERNAME_RESET_CONFIRM_URL': 'email_reset/{uid}/{token}',
    # パスワードリセット完了用URL
    'PASSWORD_RESET_CONFIRM_URL': 'password_reset/{uid}/{token}',
    # カスタムユーザー用シリアライザー
    'SERIALIZERS': {
        'user_create':  'accounts.serializers.UserSerializer',
        'user':         'accounts.serializers.UserSerializer',
        'current_user': 'accounts.serializers.UserSerializer'
    },
    'EMAIL': {
        # アカウント本登録
        'activation':                    'accounts.email.ActivationEmail',
        # アカウント本登録完了
        'confirmation':                  'accounts.email.ConfirmationEmail',
        # パスワードリセット
        'password_reset':                'accounts.email.PasswordResetEmail',
        # パスワードリセット完了
        'password_changed_confirmation': 'accounts.email.PasswordChangedConfirmationEmail',
        # メールアドレスリセット完了
        'username_changed_confirmation': 'accounts.email.UsernameChangedConfirmationEmail',
        # メールアドレスリセット
        'username_reset':                'accounts.email.UsernameResetEmail',
    }
}

# AUTH_USER_MODEL = 'accounts.UserAccount'

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'https://kasokomi.site',
    'https://www.kasokomi.site',
    'https://kasokomi-frontend.vercel.app',
    'http://127.0.0.1:8000',
    'http://localhost', 
    'http://127.0.0.1'
)

ASGI_APPLICATION = "mysite.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            # "hosts": [('127.0.0.1', 6379)],
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
            # "hosts": [os.environ.get('REDIS_URL', 6379)],
            # "hosts": [('REDIS_URL', 6379)],
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        'OPTIONS': {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEBUG = False
# DEBUG = True

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)
    import django_heroku
    django_heroku.settings(locals())