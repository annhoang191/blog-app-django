import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config("SECRET_KEY", default="")

DEBUG = True
ALLOWED_HOSTS = ["localhost", "logindjango.herokuapp.com"]

INSTALLED_APPS = [
  "blog_app.apps.BlogAppConfig",
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
]

MIDDLEWARE = [
  "whitenoise.middleware.WhiteNoiseMiddleware",
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.locale.LocaleMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "blog_project.urls"

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
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

WSGI_APPLICATION = "blog_project.wsgi.application"

DATABASES = {
    "default": {
      "ENGINE": "django.db.backends.mysql",
      "NAME": config("NAME_DB", default=""),
      "USER": config("USER_DB", default=""),
      "PASSWORD": config("PASSWORD_DB", default=""),
      "HOST": "127.0.0.1",
      "PORT": "3306",
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"

import dj_database_url
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(prod_db)

PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
  os.path.join(PROJECT_ROOT, "static"),
)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com" #
EMAIL_HOST_USER = config("USER_GMAIL", default="")
EMAIL_HOST_PASSWORD = config("PASSWORD_GMAIL", default="")
EMAIL_PORT = 587

#SETTING SEND MAIL IN  PRODUCTION WITH SENDGRID:
# EMAIL_HOST = "smtp.sendgrid.net"
# EMAIL_HOST_USER = "sendgrid_username"
# EMAIL_HOST_PASSWORD = "sendgrid_password"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# LOG SQL QUERY IN CONSOLE
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }
}
