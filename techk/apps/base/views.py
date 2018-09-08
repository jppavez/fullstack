from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect
from django.template import loader
from .models.Category import Category
from .models.Book import Book


def index(request):
    categories = Category.objects.order_by('name').all()

    template = loader.get_template('index.html')

    context = {
        'categories': categories
    }

    return HttpResponse(template.render(context, request))


def category_detail(request, category_id):

    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        raise Http404

    template = loader.get_template('category.html')

    context = {
        'category': category
    }

    return HttpResponse(template.render(context, request))


def book_detail(request, book_id):

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404

    template = loader.get_template('book.html')

    context = {
        'book': book
    }

    return HttpResponse(template.render(context, request))
