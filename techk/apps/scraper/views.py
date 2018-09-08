# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

from .providers.BooksToScrape import BooksToScrape
from apps.base.models.Category import Category
from apps.base.models.Book import Book


def scrap_main(request):
    scrap = BooksToScrape()
    categories = scrap.getCategories()

    for name, url in categories:

        # Verificar que categoria ya no exista
        category_exist = Category.objects.get(name=name)
        if category_exist:
            continue

        category = Category.create(name=name)

        books = scrap.getBookFromCategory(url)

        for book in books:
            book_name = book[0]

            book_info_url = book[1]
            title, upc, price, thumbnail, stock, stock_quantity, description = scrap.getBookInformation(
                book_info_url)
            book = Book.create(title=title,
                               upc=upc,
                               price=price,
                               thumbnail=thumbnail,
                               stock=stock,
                               stock_quantity=stock_quantity,
                               description=description)

            category.books.add(book)

    return HttpResponse("SUCCESS")
