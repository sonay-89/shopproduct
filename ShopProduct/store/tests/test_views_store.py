import pytest

@pytest.mark.django_db
def test_store_list_api(api_client, store):
    response = api_client.get("/stores/")
    print("Response status:", response.status_code)
    print("Response content:", response.content)
    assert response.status_code == 200