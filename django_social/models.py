from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(null=True, blank=True)


class Image(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(
        User, related_name='images',
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True)
