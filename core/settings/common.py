import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

import logging
from django.urls import reverse_lazy  # For generating URLs for models and views
from django.utils.translation import gettext_lazy as _  # For translation support

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")
INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.import_export",
    "unfold.contrib.filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "djoser",
    "drf_spectacular",
    "authentication",
    "store",
    "common",
    "import_export",
    "corsheaders",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../static-files")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "../media")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
EMAIL_HOST_USER = ""  # os.getenv("jo_dev_mail")
EMAIL_HOST_PASSWORD = ""  # os.getenv("jo_dev_token")
# EMAIL_USE_TLS = True
# TAGGIT_CASE_INSENSITIVE = True
# DEFAULT_FROM_EMAIL = "info@e-market.com"


REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

AUTH_USER_MODEL = "authentication.User"

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": False,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,  # tell the frontend email not found if it does not exist
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,  # send email when email/username changed
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,  # send email when password changed
    "SEND_ACTIVATION_EMAIL": True,  # send activation link to the user ,initially account is inactive
    "SEND_CONFIRMATION_EMAIL": False,  # send when user registration completed and activated
    # "ACTIVATION_URL": "activate/{uid}/{token}",
    # "SERIALIZERS": {
    #     "user_create": "authentication.serializers.UserCreateSerializer",
    #     "current_user": "authentication.serializers.UserSerializer",
    # },
    "ACTIVATION_URL": os.getenv("FRONTEND_ADDRESS") + "/account/activate/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": os.getenv("FRONTEND_ADDRESS")
    + "/account/reset/confirm/{uid}/{token}",
    "EMAIL": {
        "activation": "authentication.email.ActivationEmail",
        "confirmation": "authentication.email.ConfirmationEmail",
        "password_reset": "authentication.email.PasswordResetEmail",
        "password_changed_confirmation": "authentication.email.PasswordChangedConfirmationEmail",
        "username_reset": "authentication.email.UsernameResetEmail",
    },
}
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=6),
    "TOKEN_OBTAIN_SERIALIZER": "authentication.serializers.MyTokenObtainPairSerializer",
}
SPECTACULAR_SETTINGS = {
    "TITLE": "e-market api",
    "DESCRIPTION": "An api for a production level  e-commerce website app ,Yosef.E ",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime}  ({levelname}) | {name}| {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": ".log/general.log",
            "formatter": "verbose",
        },
        "service_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": ".log/service.log",  # Service log file
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django_service": {  # Specific logger for service logs,
            "handlers": ["service_file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

# https://docs.python.org/3/library/logging.html#logrecord-attributes


UNFOLD = {
    # "SITE_URL": "/store/",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Authorization"),
                "separator": True,
                "collapsible": False,
                "icon": "dashboard",
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:authentication_user_changelist"),
                        "separator": True,
                    },
                    {
                        "title": _("Group"),
                        "icon": "groups",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                    {
                        "title": _("Customers"),
                        "icon": "people_alt",
                        "link": reverse_lazy("admin:store_customer_changelist"),
                    },
                ],
            },
            {
                "title": _("Stor And Sales"),
                "separator": True,
                "collapsible": False,
                "icon": "dashboard",
                "items": [
                    {
                        "title": _("Product"),
                        "icon": "storefront",
                        "link": reverse_lazy("admin:store_product_changelist"),
                    },
                    {
                        "title": _("Orders"),
                        "icon": "list_alt",
                        "link": reverse_lazy("admin:store_order_changelist"),
                    },
                    {
                        "title": _("Order Items"),
                        "icon": "assignment",
                        "link": reverse_lazy("admin:store_orderitem_changelist"),
                    },
                    {
                        "title": _("Cart"),
                        "icon": "shopping_cart",
                        "link": reverse_lazy("admin:store_cart_changelist"),
                    },
                    {
                        "title": _("Cart Items"),
                        "icon": "inventory",
                        "link": reverse_lazy("admin:store_cartitem_changelist"),
                    },
                    {
                        "title": _("Collections"),
                        "icon": "collections",
                        "link": reverse_lazy("admin:store_collection_changelist"),
                    },
                ],
            },
        ],
    },
}


logging.captureWarnings(True)
CORS_ALLOWED_ORIGINS = [os.getenv("FRONTEND_ADDRESS")]
