from django.contrib import admin

from products.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name', 'description', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created", "date_of_change")
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
