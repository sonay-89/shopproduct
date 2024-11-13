from django.contrib import admin
from .models import Store
from ..products.admin import StoreProductCountInline
from ..products.models import StoreProductCount


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_prices','created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    inlines = [StoreProductCountInline]  # Возможность видеть и добавлять продукты в магазине

    def get_products(self, obj):
        return ', '.join([product.name for product in obj.products.all()])
    get_products.short_description = 'Products'

    def get_prices(self, obj):
        store_products = StoreProductCount.objects.filter(store=obj)
        return ', '.join([f'{store_product.product.name}: {store_product.product.price}' for store_product in store_products])
    get_prices.short_description = 'Product Prices'



class StoreProductCountInline(admin.TabularInline):
    model = StoreProductCount
    fields = ('product', 'get_price', 'count', 'owner')  # Используем метод для отображения цены
    readonly_fields = ('get_price',)  # Цена будет подтягиваться автоматически
    extra = 1

    def get_price(self, obj):
        return obj.product.price if obj.product else None
    get_price.short_description = 'Price'