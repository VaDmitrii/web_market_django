from rest_framework import serializers

from category.models import Category


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
    slug = serializers.CharField(min_length=5)

    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    slug = serializers.CharField(min_length=5)

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id"]
