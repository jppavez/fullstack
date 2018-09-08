from django.db import models
from .Book import Book


class Category(models.Model):
    name = models.CharField(max_length=100)

    books = models.ManyToManyField(Book, related_name='categories')

    @staticmethod
    def create(name):
        category = Category.objects.create(name=name)

        return category
