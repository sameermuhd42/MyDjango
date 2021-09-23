from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# class CustomUser(AbstractUser):
#     age = models.CharField(max_length=255)


class Book(models.Model):
    book_name = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.book_name


class Order(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    options = (('ordered', 'ordered'), ('delivered', 'delivered'), ('cancelled', 'cancelled'),
               ('intransit', 'inntransit'))
    status = models.CharField(max_length=20, choices=options, default='ordered')
    phone = models.CharField(max_length=15)
    expected_delivery_date = models.DateField(null=True, blank=True)
