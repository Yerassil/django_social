from django.contrib import admin
from django.utils.html import format_html

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'image']


admin.site.register(Image, ImageAdmin)
