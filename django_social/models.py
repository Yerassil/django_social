from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(
        User, related_name='images',
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True)
