import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from shopproduct.store.models import Store
from datetime import datetime, timezone

@pytest.fixture
def test_user(db):
    return User.objects.create_user(username="test_user", password="password")

@pytest.fixture
def store(db):
    # Создаёт магазин для использования в тестах
    return Store.objects.create(store_name="Test Store", markup_percentage=10)

@pytest.fixture
def fixed_datetime():
    return datetime(2024, 1, 1, tzinfo=timezone.utc)


@pytest.fixture
def api_client(db):
    user = User.objects.create_user(username="testuser", password="password")
    assert User.objects.filter(username="testuser").exists(), "User not created"
    client = APIClient()
    success = client.login(username="testuser", password="password")
    assert success, "Login failed"
    return client

@pytest.fixture
def owner_1(db):
    return User.objects.create_user(username="owner1", password="password")

@pytest.fixture
def owner_2(db):
    return User.objects.create_user(username="owner2", password="password")

@pytest.fixture
def stores_for_owner_1(db, owner_1):
    return [Store.objects.create(store_name=f"Store_{i}", markup_percentage=10, owner=owner_1) for i in range(7)]

@pytest.fixture
def stores_for_owner_2(db, owner_2):
    return [Store.objects.create(store_name=f"Store_{i + 7}", markup_percentage=15, owner=owner_2) for i in range(6)]



