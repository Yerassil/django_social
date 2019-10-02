from django.contrib import admin

from .models import Image, Follower, User


class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'image']


admin.site.register(Image, ImageAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'birthday'
    ]


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = [
        'follower', 'following'
    ]
