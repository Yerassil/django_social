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


class Follower(models.Model):
    follower = models.ForeignKey(
        User, related_name='following',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name='followers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return '{} follows {}'.format(
            self.follower.username,
            self.following.username
        )
