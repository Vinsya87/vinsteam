from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.signals import user_logged_in


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
