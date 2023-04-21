from django.apps import AppConfig
from grados.configs.settings.base import DEFAULT_APPS_PATH


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = DEFAULT_APPS_PATH + 'students'
