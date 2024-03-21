from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextField


class CustomUser(AbstractUser):
    bio = TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
