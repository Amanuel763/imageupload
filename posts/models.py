from distutils.command.upload import upload
from turtle import title
from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title