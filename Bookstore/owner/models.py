from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    age = models.CharField(max_length=255)


class Book(models.Model):
    book_name = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.book_name
