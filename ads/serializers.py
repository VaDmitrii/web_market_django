from rest_framework import serializers

from ads.models import Ad
from category.models import Category


class AdListSerializer(serializers.ModelSerializer):
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
    author = serializers.ReadOnlyField(source='username')
    image = serializers.ImageField(required=False)

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
    author = serializers.ReadOnlyField(source='username')
    category = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Category.objects.all()
    )

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
