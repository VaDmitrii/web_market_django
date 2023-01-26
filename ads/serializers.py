from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

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
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

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

    class Meta:
        model = Ad
        exclude = ["image"]
