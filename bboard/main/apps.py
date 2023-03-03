from django.apps import AppConfig
from django.dispatch import Signal
from main.utils import send_activation_notification

user_registered = Signal()


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Доска объявлений'

    def ready(self):
        user_registered.connect(user_registered_dispatcher)
