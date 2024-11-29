import pytest

from shopproduct.store.models import Store


@pytest.mark.django_db
def test_store_list_api(api_client, store):
    response = api_client.get("/stores/")
    print("Response status:", response.status_code)
    print("Response content:", response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_store_creation(store):
    assert Store.objects.count() == 1

@pytest.mark.django_db
def test_store_creation_with_same_name():
    # Можно создать магазин с тем же именем, потому что база данных откатывается
    Store.objects.create(store_name="Test Store", markup_percentage=20)
    assert Store.objects.count() == 1