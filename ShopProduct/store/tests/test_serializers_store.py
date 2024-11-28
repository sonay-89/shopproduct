from freezegun import freeze_time
import pytest

from shopproduct.store.models import Store
from shopproduct.store.serializers import StoreBaseSerializer, StoreDetailSerializer
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_store_base_serializer_valid_data(store):
    """Тест валидации данных для StoreBaseSerializer"""
    # Создаём пользователя
    user = User.objects.create_user(username="unic_test_user", password="password")
    # Подготавливаем данные для сериалайзера
    data = {
        "store_name": "Test Store",
        "markup_percentage": 15,
    }
    # Инициализируем сериалайзер
    serializer = StoreBaseSerializer(data=data)
    # Проверяем валидность
    assert serializer.is_valid()
    # Сохраняем объект
    store = serializer.save(owner=user)
    # Проверяем поля объекта
    assert store.store_name == "Test Store"
    assert store.markup_percentage == 15
    assert store.owner.username == "unic_test_user"


@pytest.mark.django_db
def test_store_base_serializer_invalid_data():
    """Тест невалидных данных для StoreBaseSerializer"""
    data = {
        "markup_percentage": 15  # Отсутствует store_name
    }
    # Инициализируем сериалайзер
    serializer = StoreBaseSerializer(data=data)
    # Ожидаем, что данные будут невалидными
    assert not serializer.is_valid()
    # Проверяем наличие ошибок
    assert 'store_name' in serializer.errors
    assert serializer.errors['store_name'][0] == 'This field is required.'


@pytest.mark.django_db
def test_store_base_serializer_output(store):
    """Тест сериализации объекта через StoreBaseSerializer"""
    # Создаём пользователя и магазин
    user = User.objects.create_user(username="testuser", password="password")
    store = Store.objects.create(
        store_name="Serialized Store",
        markup_percentage=10,
        owner=user
    )
    # Сериализуем объект
    serializer = StoreBaseSerializer(store)
    # Проверяем сериализованные данные
    assert serializer.data['store_name'] == "Serialized Store"
    assert serializer.data['markup_percentage'] == 10
    assert serializer.data['owner_username'] == "testuser"

@pytest.mark.django_db
def test_store_detail_serializer_output(store):
    """Тест сериализации объекта через StoreDetailSerializer"""
    from datetime import timezone

    # Замораживаем время
    with freeze_time("2024-01-01T00:00:00Z"):
        # Создаём пользователя и магазин
        user = User.objects.create_user(username="un_testuser", password="password")
        store = Store.objects.create(
            store_name="Detailed Store",
            markup_percentage=20,
            owner=user
        )

        # Сериализуем объект через StoreDetailSerializer
        serializer = StoreDetailSerializer(store)

        # Проверяем данные
        assert serializer.data['store_name'] == "Detailed Store"
        assert serializer.data['markup_percentage'] == 20
        assert serializer.data['owner_username'] == "un_testuser"
        assert serializer.data['created_at'] == "2024-01-01T00:00:00Z"
        assert serializer.data['updated_at'] == "2024-01-01T00:00:00Z"
