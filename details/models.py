from email.mime import image
from hashlib import blake2b
from django.db import models

# Create your models here.

class Sites(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'images', blank=True)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
