from rest_framework import serializers

from shopproduct.store.models import Store


class StoreBaseSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Store
        fields = ["id", "store_name", "markup_percentage", "owner_username"]  # Указываем 'id' как ID магазина

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['markup_percentage'] = float(data['markup_percentage'])  # Преобразуем в число
        return data

class StoreDetailSerializer(StoreBaseSerializer):

    class Meta(StoreBaseSerializer.Meta):
        fields = StoreBaseSerializer.Meta.fields + [
            "created_at",
            "updated_at",
        ]  # Добавляем больше информации о магазине
