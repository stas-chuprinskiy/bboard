from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_activated = models.BooleanField('Прошел активацию?', default=False)
    notify = models.BooleanField(
        'Уведомлять о новых комментариях?', default=True
    )

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.email
