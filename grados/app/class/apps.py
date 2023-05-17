from django.apps import AppConfig

from grados.configs.settings.base import DEFAULT_APPS_PATH


class ClassConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = DEFAULT_APPS_PATH + "class"
