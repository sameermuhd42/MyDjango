from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()

    def __str__(self):
        return self.book_name
