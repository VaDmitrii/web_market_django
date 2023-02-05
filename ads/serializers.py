from django.core.validators import MinLengthValidator
from rest_framework import serializers

from ads.models import Ad, Category, Selection

# from users.models import User
from users.models import User


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    slug = serializers.CharField()

    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    slug = serializers.CharField()

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id"]


class AdListSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(required=False)
    author = serializers.ReadOnlyField(source='username')

    class Meta:
        model = Ad
        fields = [
            'id',
            'name',
            'author_id',
            'author',
            'price',
            'description',
            'is_published',
            'category_id',
            'image'
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(required=False)
    author = serializers.ReadOnlyField(source='username')

    class Meta:
        model = Ad
        fields = [
            'id',
            'name',
            'author_id',
            'author',
            'price',
            'description',
            'is_published',
            'category_id',
            'image'
        ]


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.ReadOnlyField(
        required=False,
        source='username',
        default=serializers.CurrentUserDefault()
    )
    image = serializers.ImageField(required=False)
    is_published = serializers.CharField(required=False)
    name = serializers.CharField(validators=[MinLengthValidator(limit_value=10)])
    author_id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = [
            "id",
            "image",
            "name",
            "price",
            "description",
            "is_published",
            "author_id",
            "author",
            "category"
        ]


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author_id = serializers.IntegerField(required=False)
    author = serializers.ReadOnlyField(
        required=False,
        source='username',
        default=serializers.CurrentUserDefault()
    )
    category = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Category.objects.all()
    )
    is_published = serializers.CharField(required=False)
    name = serializers.CharField()

    class Meta:
        model = Ad
        fields = [
            "id",
            "name",
            "price",
            "description",
            "is_published",
            "author_id",
            "author",
            "category"
        ]


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdDetailSerializer(many=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = ["id", "items", "name", "owner"]


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Ad.objects.all()
    )
    owner = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Selection
        fields = ["id", "name", "owner", "items"]

    # def is_valid(self, *, raise_exception=False):
    #     self._items = self.initial_data.pop("items")
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def create(self, validated_data):
    #     selection = Selection.objects.create(**validated_data)
    #
    #     for item in self._items:
    #         ad = Ad.objects.get(pk=item)
    #         selection.items.add(ad)
    #
    #         selection.save()
    #
    #     return selection


class SelectionUpdateSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        required=False,
        many=True,
        queryset=Ad.objects.all()
    )
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = ["id", "name", "owner", "items"]

    # def is_valid(self, *, raise_exception=False):
    #     self._items = self.initial_data.pop("items", None)
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def save(self, request):
    #     selection = super().save()
    #
    #     if self._items:
    #         for item in self._items:
    #             item = Ad.objects.get(pk=item)
    #             selection.items.add(item)
    #
    #         selection.save()
    #
    #     return selection


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]
