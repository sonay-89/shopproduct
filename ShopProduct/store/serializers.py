from rest_framework import serializers

from ShopProduct.products.models import StoreProductCount
from ShopProduct.store.models import Store


class StoreSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()  # Поле для отображения всех продуктов
    # Example:
    # products = ProductsSerializer # reed source in serial
    class Meta:
        model = Store
        fields = ['id', 'name', 'products']

    def get_products(self, obj):
        # Получаем все записи StoreProductCount, связанные с данным магазином
        store_product_counts = StoreProductCount.objects.filter(store=obj)
        # Используем StoreProductCountSerializer для отображения информации о продукте и количестве
        return StoreProductCountSerializer(store_product_counts, many=True).data

class StoreProductCountSerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(source='store.name', read_only=True)  # Подтягиваем имя магазина
    product_name = serializers.CharField(source='product.name', read_only=True)  # Подтягиваем имя продукта
    price = serializers.DecimalField(source='product.price', max_digits=20, decimal_places=2, read_only=True)


    class Meta:
        model = StoreProductCount
        fields = ['id', 'store', 'store_name', 'product', 'product_name', 'count','price' ]

# TODO необходимо сделать разделение(с наследованием(!)), есть базовый сериалйзер продукта, магазина и т.д,
#  который в общем списке выводит базовую информацию, к примеру название магазина+кол-во и название продукта. Это надо использовать для полного списка магазинов
# + сделать сериайлезр для конкретного магазина, который позволит уже выводить и цену. разные  Сериайлезеры(базовый и нет) наследуется.

# TODO если это ID, указывай что это именно айди