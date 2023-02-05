import factory.django

from ads.models import Ad, Category, Selection
# from category.models import Category
# from selection.models import Selection
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "cats"
    slug = "cats_cat"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test_user"
    password = "test123"
    date_of_birth = "2000-01-22"
    email = "tests@test.ru"
    role = "moderator"
    is_active = True


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test_advertising"
    author = factory.SubFactory(UserFactory)
    price = 100
    description = "None"
    is_published = False
    category = factory.SubFactory(CategoryFactory)
    image = None


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "test selection"
    owner = factory.SubFactory(UserFactory)
    items = factory.RelatedFactoryList(AdFactory)
