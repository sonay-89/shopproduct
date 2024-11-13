# products/admin.py
from django.contrib import admin
from .models import Product, StoreProductCount

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price',)  # Укажите, какие поля отображать
    search_fields = ('product_name',)       # Добавьте поле для поиска

class StoreProductCountInline(admin.TabularInline):
    model = StoreProductCount
    fields = ('product_name', 'store_name', 'count', 'owner', 'store_price')  # Используем метод для отображения цены
    readonly_fields = ('store_price',)

