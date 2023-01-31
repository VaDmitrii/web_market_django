import pytest

from tests.factories import UserFactory
from users.models import User


@pytest.fixture
@pytest.mark.django_db
def user_token_jwt(client):
    username = 'test_user'
    password = 'test123'

    user = User.objects.last()
    user.set_password(password)
    user.save()

    response = client.post(
        '/user/token/',
        data={'username': username, 'password': password},
        format='json'
    )

    return response.data['access']
