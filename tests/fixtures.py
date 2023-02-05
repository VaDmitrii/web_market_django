import pytest

from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient():
    return APIClient()

# @pytest.mark.django_db
# def user_token_jwt(client):
#     username = 'test_user'
#     password = 'test123'
#
#     user = User.objects.last()
#     user.set_password(password)
#     user.save()
#
#     response = client.post(
#         '/user/token/',
#         data={'username': username, 'password': password},
#         format='json'
#     )
#
#     return response.data['access']
