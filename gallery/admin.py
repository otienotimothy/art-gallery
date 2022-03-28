from django.contrib import admin
from .models import Photo, Location, Category

# Register your models here.
admin.site.register(Photo)
admin.site.register(Location)
admin.site.register(Category)