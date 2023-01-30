import pytest

from ads.serializers import AdListSerializer, AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client, ad):
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            'id': ad.pk,
            'name': 'test',
            'author_id': ad.author_id_id,
            'author': ad.username,
            'price': 100,
            'description': 'None',
            'is_published': 'FALSE',
            'category_id': ad.category_id,
            'image': None
        }]
    }

    response_list = client.get("/ad/")

    assert response_list.status_code == 200
    assert response_list.data == expected_response


@pytest.mark.django_db
def test_one_ad(client, ad):
    expected_response = {
        'id': ad.pk,
        'name': 'test',
        'author_id': ad.author_id_id,
        'author': ad.username,
        'price': 100,
        'description': 'None',
        'is_published': 'FALSE',
        'category_id': ad.category_id,
        'image': None
    }

    response = client.get(f"/ad/{ad.pk}/")

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad(client, ad, user_token_jwt):
    # user_token_jwt = client.post(
    #     "/user/token/",
    #     {"username": "test_user", "password": "test123"},
    #     content_type="application/json"
    # )

    expected_response = {
        'id': ad.pk,
        'name': 'test',
        'author_id': ad.author_id_id,
        'author': ad.username,
        'price': 100,
        'description': 'None',
        'is_published': 'FALSE',
        'category_id': ad.category_id,
        'image': None
    }

    data = {
        "name": "test",
        "price": 100,
        "description": "None",
        "author_id": ad.author_id,
        "category": ad.category_id,
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer" + user_token_jwt
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_selection_create(client, selection, user_token_jwt):
    expected_response = {
        "id": 1,
        "name": selection.name,
        "owner": selection.owner.username,
        "items": AdListSerializer(many=True).data
    }

    data = {
        "name": selection.name,
        "items": AdListSerializer(many=True)
    }

    response = client.post(
        "/selection/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer" + user_token_jwt
    )

    assert response.status_code == 201
    assert response.data == expected_response
