from rest_framework import serializers

from shopproduct.store.models import Store


class StoreBaseSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    markup_percentage = serializers.FloatField()
    class Meta:
        model = Store
        fields = ["id", "store_name", "markup_percentage", "owner_username"]  # Указываем 'id' как ID магазина

class StoreDetailSerializer(StoreBaseSerializer):

    class Meta(StoreBaseSerializer.Meta):
        fields = StoreBaseSerializer.Meta.fields + [
            "created_at",
            "updated_at",
        ]  # Добавляем больше информации о магазине
