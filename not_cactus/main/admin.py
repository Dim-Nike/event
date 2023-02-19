from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['categories', 'name', 'price', 'count_product', 'is_active']
    list_filter = ['categories', 'is_active']
    search_fields = ['name']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product, ProductAdmin)