from django.db import models


class Book(models.Model):
    title = models.TextField()
    thumbnail = models.URLField()
    price = models.FloatField()
    upc = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.BooleanField(default=False)
    stock_quantity = models.IntegerField()

    @staticmethod
    def create(title, upc, price, thumbnail, stock, stock_quantity, description):
        book = Book.objects.create(
            title=title,
            upc=upc,
            price=price,
            thumbnail=thumbnail,
            stock=stock,
            stock_quantity=stock_quantity,
            description=description
        )
        return book
