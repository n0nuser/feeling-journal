from django.core.exceptions import ImproperlyConfigured
from unipath import Path
import environ
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
env = environ.FileAwareEnv()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
PROJECT_DIR = Path(__file__).parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="mySecretDummyKey")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=False)

SERVER = env("SERVER_HOST", default="localhost")
PORT = env("SERVER_PORT", default="80,443").split(",")

INTERNAL_IPS = ["127.0.0.1", "localhost"]

_DEFAULT_CLIENT_HOSTS = ["*"]
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="localhost,127.0.0.1").split(",")
if not ALLOWED_HOSTS:
    if not DEBUG:
        raise ImproperlyConfigured("ALLOWED_CLIENT_HOSTS environment variable must be set when DEBUG=False.")
    ALLOWED_CLIENT_HOSTS = _DEFAULT_CLIENT_HOSTS

CSRF_TRUSTED_ORIGINS = []
for port in PORT:
    if port == "80":
        for host in ALLOWED_HOSTS:
            CSRF_TRUSTED_ORIGINS.extend((f"http://*.{host}",))
    if port == "443":
        for host in ALLOWED_HOSTS:
            CSRF_TRUSTED_ORIGINS.extend((f"https://*.{host}",))
    if port not in ["80", "443"]:
        for host in ALLOWED_HOSTS:
            CSRF_TRUSTED_ORIGINS.extend((f"http://*.{host}:{port}", f"https://*.{host}:{port}"))


# Application definition
# Don't Modify the Order of the Apps!!!!
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.admin",
    "authentication",
    "web",
    "crispy_forms",
    "tempus_dominus",
    "import_export",
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "core.urls"
CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_REDIRECT_URL = "home"  # Route defined in web/urls.py
LOGOUT_REDIRECT_URL = "login"  # Route defined in web/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")  # ROOT dir for templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": "postgres",  # Taken from docker-compose.yml
            "PORT": 5432,
            "NAME": env("POSTGRES_NAME", default="postgres"),
            "USER": env("POSTGRES_USER", default="postgres"),
            "PASSWORD": env("POSTGRES_PASSWORD", default="postgres"),
        }
    }



# Authentication
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#writing-an-authentication-backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = "authentication.CustomUser"

# Cache
# https://docs.djangoproject.com/en/4.0/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

APPEND_SLASH = True

# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "": {  # 'catch all' loggers by referencing it with the empty string
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = str(env('EMAIL_HOST', default='smtp.gmail.com'))  # add your own settings here
EMAIL_PORT = int(env('EMAIL_PORT', default=587))  # add your own settings here
EMAIL_HOST_USER = str(env('EMAIL_HOST_USER', default='account@gmail.com'))  # add your own settings here
EMAIL_HOST_PASSWORD = str(env('EMAIL_HOST_PASSWORD', default='password'))  # add your own settings here
EMAIL_USE_TLS = True  # add your own settings here
