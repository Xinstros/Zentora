from django.db import models
from django.contrib.auth.models import AbstractUser

class ZentoraUser(AbstractUser):
    ACCOUNT_TYPES = (
        ('DEV', 'Developer'),
        ('USER', 'Regular User'),
    )
    account_type = models.CharField(max_length=4, choices=ACCOUNT_TYPES, default='USER')
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

class Task(models.Model):
    user = models.ForeignKey('ZentoraUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TODO')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Request(models.Model):
    user = models.ForeignKey('ZentoraUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    style = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    deadline = models.DateField()
    reward_type = models.CharField(max_length=10, choices=[('CASH', 'Cash'), ('CRYPTO', 'Crypto')])
    reward_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Artwork(models.Model):
    user = models.ForeignKey('ZentoraUser', on_delete=models.CASCADE)
    file = models.FileField(upload_to='artwork/')
    title = models.CharField(max_length=200)
    license = models.CharField(max_length=10, choices=[('FREE', 'Free'), ('CC0', 'CC0'), ('PAID', 'Paid')])
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title