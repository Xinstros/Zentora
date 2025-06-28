from django.db import models
from django.contrib.auth.models import AbstractUser

class ZentoraUser(AbstractUser):
    ACCOUNT_TYPES = (
        ('DEV', 'Developer'),
        ('USER', 'Regular User'),
    )
    account_type = models.CharField(max_length=4, choices=ACCOUNT_TYPES, default='USER')