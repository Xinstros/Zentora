from django.db import models
from django.contrib.auth.models import AbstractUser

class ZentoraUser(AbstractUser):
    ACCOUNT_TYPES = (
        ('DEV', 'Developer'),
        ('USER', 'Regular User'),
    )
    account_type = models.CharField(max_length=4, choices=ACCOUNT_TYPES, default='USER')

class Task(models.Model):
    user = models.ForeignKey('ZentoraUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TODO')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title