from django.apps import AppConfig


class LibraryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.music_app'

    def ready(self):
        from . import signals
