from django.contrib import admin

from images.models import Image


@admin.register(Image)
class ImageModel(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']