from .common import *

DEBUG = False
ALLOWED_HOSTS = [
    "info.jos.com",
]
# replace with production  database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.getenv("DBNAME"),
#         "HOST": os.getenv("DBHOST"),
#         "USER": os.getenv("DBUSER"),
#         "PASSWORD": os.getenv("DBPASSWORD"),
#     }
# }
