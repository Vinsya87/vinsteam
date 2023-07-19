from django.apps import AppConfig


class ConfigSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config_site'
    verbose_name = 'Настройки сайта'
