from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from products.models import Product, Category

def product(request: HttpRequest, product_id: int):
    """представление страницы main/product.html для каждого продукта"""
    prod_get = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product.html', {'product': prod_get})

def home(request: HttpRequest):
    """Список товаров"""
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'products/home.html', context)

