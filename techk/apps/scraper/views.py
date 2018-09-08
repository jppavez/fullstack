# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

from .providers.BooksToScrape import BooksToScrape
from apps.base.models.Category import Category
from apps.base.models.Book import Book


def test(request):
    scrap = BooksToScrape()
    categories = scrap.getCategories()

    for name, url in categories:
        category = Category.create(name=name)

        if name != "Fantasy":
            continue

        books = scrap.getBookFromCategory(url)

        for book in books:
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

    return JsonResponse(dict(categories))
