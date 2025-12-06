import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# basic django settings file, trying to keep it simple
BASE_DIR = Path(__file__).resolve().parent.parent



# probably should change this in real prod
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-dad6jf3#2ihwyc&!x@_=38^7@ago2(c1^t0wwda9_(ogewt6j0)')

DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS_STR = os.getenv('DJANGO_ALLOWED_HOSTS', '')
if ALLOWED_HOSTS_STR:
    ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_STR.split(',') if host.strip()]
else:
    ALLOWED_HOSTS = ['*']                                 

CSRF_TRUSTED_ORIGINS_STR = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS', '')
if CSRF_TRUSTED_ORIGINS_STR:
    CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in CSRF_TRUSTED_ORIGINS_STR.split(',') if origin.strip()]
else:
    CSRF_TRUSTED_ORIGINS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aurelion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aurelion.wsgi.application'


# just using sqlite here so it works out of the box
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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



LANGUAGE_CODE = 'en-us'

def detect_system_timezone():
    """
    Pick up the local machine timezone (or env override) so displayed times
    match the host without hardcoding a region. Works across Linux/macOS/Windows
    when tzdata is available.
    """
    def _validate_tz(name):
        try:
            ZoneInfo(name)
            return name
        except Exception:
            return None

    env_tz = os.getenv('DJANGO_TIME_ZONE') or os.getenv('TZ')
    if env_tz and _validate_tz(env_tz):
        return env_tz

    def _from_path(path):
        try:
            real = os.path.realpath(path)
            parts = real.split(os.sep)
            tz_name = None
            for i, p in enumerate(parts):
                if p.startswith('zoneinfo') and i + 1 < len(parts):
                    tz_name = '/'.join(parts[i + 1 :])
                    break
            if tz_name and _validate_tz(tz_name):
                return tz_name
        except Exception:
            return None
        return None
    for candidate in ['/etc/localtime', '/var/db/timezone/localtime']:
        tz_name = _from_path(candidate)
        if tz_name:
            return tz_name
    try:
        with open('/etc/timezone', 'r') as fh:
            tz_name = fh.read().strip()
            if tz_name and _validate_tz(tz_name):
                return tz_name
    except Exception:
        pass
    try:
        # tzlocal handles Windows and Unix; returns canonical IANA names when tzdata is installed
        import tzlocal
        tz_name = tzlocal.get_localzone_name()
        if tz_name and _validate_tz(tz_name):
            return tz_name
    except Exception:
        pass
    try:
        tzinfo = datetime.now().astimezone().tzinfo
        tz_name = getattr(tzinfo, 'key', None) or getattr(tzinfo, 'zone', None) or tzinfo.tzname(None)
        if tz_name and _validate_tz(tz_name):
            return tz_name
    except Exception:
        pass
    return 'UTC'

TIME_ZONE = detect_system_timezone()

USE_I18N = True

USE_TZ = True



# static files config, for css/js/images
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'aurelion': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
    },
}
