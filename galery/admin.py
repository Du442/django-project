from django.contrib import admin
from galery.models import Photos

class ListPhotos(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle")
    list_display_links = ("id", "name")
    search_fields = ("name", "category")

admin.site.register(Photos, ListPhotos)