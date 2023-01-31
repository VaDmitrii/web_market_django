import pytest

from ads.serializers import AdDetailSerializer, AdListSerializer


@pytest.mark.django_db
def test_ads_list(client, ad, user_token_jwt):
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            'id': ad.pk,
            'name': 'test_advertising',
            'author_id': ad.author_id_id,
            'author': ad.username,
            'price': 100,
            'description': 'None',
            'is_published': 'FALSE',
            'category_id': ad.category_id,
            'image': None
        }]
    }

    response_list = client.get(
        '/ad/',
        **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    )

    assert response_list.status_code == 200
    assert response_list.data == expected_response


@pytest.mark.django_db
def test_one_ad(client, ad, user_token_jwt):
    expected_response = {
        'id': ad.pk,
        'name': 'test_advertising',
        'author_id': ad.author_id_id,
        'author': ad.username,
        'price': 100,
        'description': 'None',
        'is_published': 'FALSE',
        'category_id': ad.category_id,
        'image': None
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    )

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad(client, ad, user_token_jwt):
    expected_response = {
        'id': 4,
        'name': ad.name,
        'author_id': ad.author_id_id,
        'author': ad.username,
        'price': 100,
        'description': 'None',
        'category': ad.category_id,
        'is_published': '',
        'image': None
    }

    data = {
        "name": "test_advertising",
        "price": 100,
        "description": "None",
        "author_id": ad.author_id_id,
        "category": ad.category_id,
    }
    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json',
        **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    )
    print(response.data)

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_selection_create(client, ad, selection, user_token_jwt):
    expected_response = {
        "id": 2,
        "name": selection.name,
        "owner": selection.owner.id,
        "items": [AdDetailSerializer(ad).data.get('id')]
    }

    data = {
        "name": selection.name,
        "items": AdDetailSerializer(ad).data.get('id')
    }

    response = client.post(
        '/selection/create/',
        data,
        content_type='application/json',
        **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    )

    assert response.status_code == 201
    assert response.data == expected_response
