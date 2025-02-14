import pytest
from users.models import User
from tests.fixtures import api_client


@pytest.mark.django_db
def test_create_user(api_client):

    data = {
        "email": "test@example.com",
        "password": "test1234",
        "first_name": "test",
        "last_name": "test"
    }

    response = api_client.post(f'/users/register/', data, format='json')

    assert response.status_code == 201
    assert User.objects.filter(email="test@example.com").exists()
