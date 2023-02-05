import pytest

from ads.models import Ad
from ads.serializers import AdDetailSerializer


@pytest.mark.django_db
def test_ads_list(client, ad):
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            'id': ad.pk,
            'name': 'test_advertising',
            'author_id': ad.author_id,
            'author': ad.author.username,
            'price': 100,
            'description': 'None',
            'is_published': False,
            'category_id': ad.category_id,
            'image': None
        }]
    }

    user = ad.author
    user.set_password(user.password)
    user.save()

    client.force_authenticate(user)
    response_list = client.get('/ad/')

    # response_list = client.get(
    #     '/ad/',
    #     **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    # )

    assert response_list.status_code == 200
    assert response_list.data == expected_response


@pytest.mark.django_db
def test_one_ad(client, ad):
    expected_response = {
        'id': ad.pk,
        'name': 'test_advertising',
        'author_id': ad.author_id,
        'author': ad.author.username,
        'price': 100,
        'description': 'None',
        'is_published': False,
        'category_id': ad.category_id,
        'image': None
    }
    user = ad.author
    user.set_password(user.password)
    user.save()

    client.force_authenticate(user)
    response = client.get(f'/ad/{ad.pk}/')

    # response = client.get(
    #     f"/ad/{ad.pk}/",
    #     **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    # )

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad(client, ad):
    expected_response = {
        'id': 4,
        'name': ad.name,
        'author_id': ad.author_id,
        'author': ad.author.username,
        'price': 100,
        'description': 'None',
        'category': ad.category_id,
        'is_published': 'False',
        'image': None
    }

    data = {
        "name": "test_advertising",
        "price": 100,
        "description": "None",
        "author_id": ad.author_id,
        "category": ad.category_id,
    }

    user = ad.author
    user.set_password(user.password)
    user.save()

    client.force_authenticate(user)
    response = client.post(
        '/ad/create/',
        data=data
    )
    # response = client.post(
    #     '/ad/create/',
    #     data,
    #     content_type='application/json',
    #     **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    # )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_selection_create(client, selection):
    user = selection.owner
    user.set_password(user.password)
    user.save()

    client.force_authenticate(user)

    expected_response = {
        "id": 2,
        "name": selection.name,
        "owner": selection.owner.id,
        "items": AdDetailSerializer(selection.items.all(), many=True).data
    }

    data = {
        "name": selection.name,
        "items": selection.items.all()
    }

    response = client.post(
        '/selection/create/',
        data=data
    )
    print(response.data)

    # response = client.post(
    #     '/selection/create/',
    #     data,
    #     content_type='application/json',
    #     **{'HTTP_AUTHORIZATION': f'Bearer {user_token_jwt}'}
    # )

    assert response.status_code == 201
    assert response.data == expected_response
