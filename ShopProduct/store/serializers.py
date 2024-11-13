from rest_framework import serializers

from ShopProduct.store.models import Store


# TODO необходимо сделать разделение(с наследованием(!)), есть базовый сериалйзер продукта, магазина и т.д,
#  который в общем списке выводит базовую информацию, к примеру название магазина+кол-во и название продукта. Это надо использовать для полного списка магазинов
# + сделать сериайлезр для конкретного магазина, который позволит уже выводить и цену. разные  Сериайлезеры(базовый и нет) наследуется.

# TODO если это ID, указывай что это именно айди

class StoreBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'markup_percentage', 'owner']  # Указываем 'id' как ID магазина

# Детализированный сериализатор для магазина, который наследуется от базового
class StoreDetailSerializer(StoreBaseSerializer):

    class Meta(StoreBaseSerializer.Meta):
        fields = StoreBaseSerializer.Meta.fields + ['created_at', 'updated_at']  # Добавляем больше информации о магазине
