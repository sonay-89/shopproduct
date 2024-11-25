from rest_framework import serializers

from shopproduct.products.models import Product, StoreProductCount


class ProductBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "product_name", "price"]  # Указываем, что 'id' — это ID продукта
        extra_kwargs = {"id": {"label": "Product ID"}}  # Чтобы было явно понятно, что это ID


class ProductDetailSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields  # Добавляем поля, которых нет в базовом сериализаторе


class StoreProductBaseSerializer(serializers.ModelSerializer):
    store = serializers.CharField()
    product = serializers.CharField()

    class Meta:
        model = StoreProductCount
        fields = ["store", "count", "product", "store_price"]
