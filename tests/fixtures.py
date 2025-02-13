import pytest
from rest_framework.test import APIClient
from network.models import NetworkNode, Product
from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def active_user(db):
    user = User.objects.create(email="test@example.com", password="password", is_active=True)
    return user


@pytest.fixture
def network_node(db):
    return NetworkNode.objects.create(
        name="Test Node",
        email="test@example.com",
        country="USA",
        city="New York",
        street="5th Avenue",
        house_number="10",
        debt=100.50
    )


@pytest.fixture
def product(db, network_node):
    return Product.objects.create(
        name="Test Product",
        model="123",
        release_date="2023-01-01",
        network_node=network_node
    )