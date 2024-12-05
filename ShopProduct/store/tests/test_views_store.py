import pytest
import logging

from rest_framework import status
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


@pytest.mark.django_db
def test_store_detail_retrieve(api_client_with_token, stores_for_owner_1, store):
    """Тест получения данных магазина владельцем."""
    store = stores_for_owner_1[0]  # Берем первый магазин из фикстуры
    url = f"/stores/{store.id}/"  # Учитываем префикс "stores/"

    # Проверка аутентификации
    response = api_client_with_token.get(url)
    assert response.status_code == status.HTTP_200_OK, f"Response: {response.content}"

    # Отладочный вывод
    print(f"Store ID: {store.id}, Store Owner ID: {store.owner.id}")

    # Проверяем содержимое ответа
    response_data = response.json()
    assert response_data["id"] == store.id
    assert response_data["store_name"] == store.store_name


@pytest.mark.django_db
def test_store_update(api_client_with_token, stores_for_owner_1, store):
    """Тест обновления данных магазина владельцем."""
    store = stores_for_owner_1[0]  # Берем первый магазин текущего пользователя
    url = f"/stores/{store.id}/"  # Учитываем префикс "stores/"
    data = {"store_name": "Updated Store", "markup_percentage": 20}

    # Выполняем PUT-запрос
    response = api_client_with_token.put(url, data, format="json")

    # Проверяем статус ответа
    assert response.status_code == status.HTTP_200_OK

    # Проверяем, что данные были обновлены в базе
    updated_store = Store.objects.get(id=store.id)
    assert updated_store.store_name == "Updated Store"
    assert updated_store.markup_percentage == 20


@pytest.mark.django_db
def test_store_delete(api_client_with_token, stores_for_owner_1, store):
    """Тест удаления магазина владельцем."""
    store = stores_for_owner_1[0]  # Берем первый магазин текущего пользователя
    url = f"/stores/{store.id}/"  # Учитываем префикс "stores/"

    # Выполняем DELETE-запрос
    response = api_client_with_token.delete(url)

    # Проверяем статус ответа
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Убеждаемся, что магазин удален из базы
    assert not Store.objects.filter(id=store.id).exists()


@pytest.mark.django_db
def test_store_detail_not_owner(api_client_with_token, stores_for_owner_2, store):
    """Тест попытки получения данных магазина, который не принадлежит пользователю."""
    store = stores_for_owner_2[0]  # Берем первый магазин другого пользователя
    url = f"/stores/{store.id}/"  # Учитываем префикс "stores/"
    response = api_client_with_token.get(url)  # Выполняем GET-запрос

    # Проверяем, что доступ запрещен (404)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Проверяем содержимое ответа
    response_data = response.json()
    assert response_data == {"detail": "Not found."}