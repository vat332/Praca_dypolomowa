from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page = models.IntegerField()
    publisher = models.CharField(max_length=255)