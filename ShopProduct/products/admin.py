# products/admin.py
from django.contrib import admin
from .models import Product, StoreProductCount


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)  # Укажите, какие поля отображать
    search_fields = ('name',)       # Добавьте поле для поиска
    # list_filter = ('store',)
# Register your models here.


class StoreProductCountInline(admin.TabularInline):
    model = StoreProductCount
    extra = 1