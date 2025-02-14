import pytest
from network.models import NetworkNode
from tests.fixtures import api_client, network_node, active_user


@pytest.mark.django_db
def test_get_network_nodes(api_client, active_user, network_node):
    api_client.force_authenticate(user=active_user)

    response = api_client.get(f'/network/nodes/')

    assert response.status_code == 200
    assert response.data[0]['name'] == network_node.name


@pytest.mark.django_db
def test_get_the_network_node(api_client, active_user, network_node):
    api_client.force_authenticate(user=active_user)

    response = api_client.get(f'/network/nodes/{network_node.id}/')

    assert response.status_code == 200
    assert response.data['name'] == 'Test Node'


@pytest.mark.django_db
def test_create_network_node(api_client, active_user):
    api_client.force_authenticate(user=active_user)
    data = {
        "name": "New Node",
        "email": "newnode@example.com",
        "country": "USA",
        "city": "Los Angeles",
        "street": "Sunset Blvd",
        "house_number": "20",
        "debt": "50.00"
    }

    response = api_client.post(f'/network/nodes/', data, format='json')

    assert response.status_code == 201
    assert NetworkNode.objects.count() == 1


@pytest.mark.django_db
def test_update_network_node(api_client, active_user, network_node):
    api_client.force_authenticate(user=active_user)
    data = {'name': 'New Name'}

    response = api_client.patch(f'/network/nodes/{network_node.id}/', data, format='json')

    assert response.data['name'] == 'New Name'


@pytest.mark.django_db
def test_delete_network_node(api_client, active_user, network_node):
    api_client.force_authenticate(user=active_user)
    data = {'name': 'New Name'}

    response = api_client.delete(f'/network/nodes/{network_node.id}/', data, format='json')

    assert response.status_code == 204


@pytest.mark.django_db
def test_filter_network_nodes(api_client, active_user, network_node):
    api_client.force_authenticate(user=active_user)
    url = f'/network/nodes/' + f'?city={network_node.city}'

    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['city'] == network_node.city
