import pytest

from users.models import User


@pytest.fixture
@pytest.mark.django_db
def user_token_jwt(client, user):
    username = "test_user"
    password = "test123"

    # user = User.objects.get(id=4)
    # user.is_active = True
    # user.save()

    # django_user_model.objects.create(
    #     username=username, password=password
    # )

    response = client.post(
        "/user/token/",
        {"username": user.username, "password": password},
        format="json"
    )

    return response.data["access"]

