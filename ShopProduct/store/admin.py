from django.contrib import admin
from .models import Store
from ..products.admin import StoreProductCountInline
from ..products.models import StoreProductCount


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("id", "store_name", "markup_percentage", "created_at", "updated_at", "owner")
    search_fields = ("store_name",)
    list_filter = ("created_at", "updated_at")
    inlines = [StoreProductCountInline]  # Возможность видеть и добавлять продукты в магазине

    def get_products(self, obj):
        return ", ".join([product_name.name for product_name in obj.products.all()])

    get_products.short_description = "Products"


class StoreProductCountInline(admin.TabularInline):
    model = StoreProductCount
    fields = ("product", "get_price", "count", "owner")  # Используем метод для отображения цены
    readonly_fields = ("get_price",)  # Цена будет подтягиваться автоматически
    extra = 1

    def get_price(self, obj):
        return obj.product.price if obj.product else None

    get_price.short_description = "Price"
