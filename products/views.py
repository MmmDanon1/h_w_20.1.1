from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from products.models import Product, Category


def product(request: HttpRequest):
    """представление страницы main/product.html для каждого продукта"""
    products_list = Product.objects.all()
    context = {
        "object_list": products_list
    }
    return render(request, 'products/product.html', context)
