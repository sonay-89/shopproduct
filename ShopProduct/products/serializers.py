from rest_framework import serializers
from ShopProduct.products.models import Product, StoreProductCount
from ShopProduct.store.models import Store


class ProductSerializer(serializers.ModelSerializer):
    store_ids = serializers.PrimaryKeyRelatedField(
        queryset=Store.objects.all(),
        many=True,
        write_only=True,
        source='store'
    )
    stores = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'store_ids', 'stores',]

    def get_stores(self, obj):
        # Получаем все магазины через промежуточную таблицу StoreProductCount
        stores = StoreProductCount.objects.filter(product=obj).select_related('store')
        return [{'id': store.store.id, 'name': store.store.name} for store in stores]

    def create(self, validated_data):
        store_ids = validated_data.pop('store', [])
        product = Product.objects.create(**validated_data)

        # Создаем связи в промежуточной таблице StoreProductCount
        for store in store_ids:
            StoreProductCount.objects.create(product=product, store=store, count=0)  # count можно указать при необходимости

        return product


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'price', 'store']
#
