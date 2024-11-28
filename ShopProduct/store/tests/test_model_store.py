import pytest

from shopproduct.store.models import Store


@pytest.mark.django_db
def test_store_creation(test_user, store):
    store = Store.objects.create(store_name="New Store", owner=test_user)
    assert store.store_name == "New Store"
    assert store.owner.username == "test_user"
