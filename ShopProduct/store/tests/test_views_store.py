import pytest
import logging

from rest_framework.test import APIClient

from shopproduct.store.models import Store


logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_store_list_api(api_client_with_token, stores_for_owner_1, stores_for_owner_2, store):
    # Выполняем GET-запрос к API
    response = api_client_with_token.get("/stores/")
    assert response.status_code == 200  # Убедись, что статус ответа успешный

    # Проверяем, что вернулись только магазины owner_1
    data = response.json()
    assert len(data) == 7
    for store in data:
        assert store["owner_username"] == "owner1"

@pytest.mark.django_db
def test_store_creation(store):
    assert Store.objects.count() == 1

@pytest.mark.django_db
def test_store_creation_with_same_name():
    # Можно создать магазин с тем же именем, потому что база данных откатывается
    Store.objects.create(store_name="Test Store", markup_percentage=20)
    assert Store.objects.count() == 1