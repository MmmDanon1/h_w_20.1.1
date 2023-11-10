from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from products.models import Product, Category
from django.views.generic import DetailView, ListView

class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product


