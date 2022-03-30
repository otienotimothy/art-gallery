
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Photo(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.RESTRICT)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)

    def __str__(self):
        return self.image_name

class Location(models.Model):
    photo_location = models.CharField(max_length=100)

    def __str__(self):
        return self.photo_location


class Category(models.Model):
    photo_category = models.CharField(max_length=100)

    def __str__(self):
        return self.photo_category
