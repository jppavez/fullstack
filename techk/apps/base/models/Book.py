from django.db import models


class Book(models.Model):
    title = models.TextField()
    thumbnail = models.URLField()
    price = models.FloatField()
    upc = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.BooleanField(default=False)
    stock_quantity = models.IntegerField()
