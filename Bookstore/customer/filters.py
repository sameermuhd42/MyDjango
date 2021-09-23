import django_filters
from owner import models


class BookFilter(django_filters.Filter):
    class Meta:
        model = models.Book
        fields = ['book_name', 'author', 'price']
