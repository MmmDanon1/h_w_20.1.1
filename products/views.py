from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from products.models import Product, Category
from django.views.generic import DetailView, ListView

class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product

# def product(request: HttpRequest, product_id: int):
#     """представление страницы blog/product_detail.html для каждого продукта"""
#     prod_get = get_object_or_404(Product, pk=product_id)
#     return render(request, 'products/product_detail.html', {'product': prod_get})
#
# def home(request: HttpRequest):
#     """Список товаров"""
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(request, 'products/product_list.html', context)

