import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from shopproduct.store.models import Store
from datetime import datetime, timezone

@pytest.fixture
def test_user(db):
    return User.objects.create_user(username="test_user", password="password")

@pytest.fixture
def store(test_user):
    return Store.objects.create(store_name="Test Store", owner=test_user)

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