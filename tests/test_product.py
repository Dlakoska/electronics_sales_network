import pytest
from tests.fixtures import api_client, product, active_user, network_node


@pytest.mark.django_db
def test_create_product(api_client, active_user, product, network_node):
    api_client.force_authenticate(user=active_user)
    data = {
        "name": "New Product",
        "model": "Z900",
        "release_date": "2024-02-01",
        "network_node": network_node.id
    }
    response = api_client.post(f'/network/products/', data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_get_product_list(api_client, active_user, product, network_node):
    api_client.force_authenticate(user=active_user)

    response = api_client.get(f'/network/products/')

    assert response.status_code == 200
    assert response.data[0]['name'] == product.name


@pytest.mark.django_db
def test_retrieve_product(api_client, active_user, product):
    api_client.force_authenticate(user=active_user)

    response = api_client.get(f'/network/products/{product.pk}/')

    assert response.status_code == 200
    assert response.data['name'] == product.name


@pytest.mark.django_db
def test_update_product(api_client, active_user, product):
    api_client.force_authenticate(user=active_user)
    data = {"name": "Новое имя"}

    response = api_client.patch(f'/network/products/{product.pk}/', data, format='json')

    assert response.status_code == 200
    product.refresh_from_db()
    assert product.name == "Новое имя"


@pytest.mark.django_db
def test_delete_product(api_client, active_user, product):
    api_client.force_authenticate(user=active_user)

    response = api_client.delete(f'/network/products/{product.pk}/'
                                 )
    assert response.status_code == 204

