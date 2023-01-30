import re

from rest_framework import serializers
from datetime import date

from users.models import User, Location


def age_min(value: date):
    if date.today().year - value.year < 9:
        raise serializers.ValidationError(
            "User must be at least 9 years old"
        )


def clean_email(email: str):
    pattern = re.compile(r"rambler\.ru", re.IGNORECASE)
    email = email.split('@')
    if pattern.match(email[1]):
        raise serializers.ValidationError(
            f"{email[1]} is of not acceptable domain"
        )


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    email = serializers.CharField(required=True, validators=[clean_email])
    date_of_birth = serializers.DateField(required=True, validators=[age_min])

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data.get("password"))
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    role = serializers.CharField(read_only=True)
    email = serializers.CharField(required=False, validators=[clean_email])
    date_of_birth = serializers.DateField(required=False, validators=[age_min])

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "role",
            "age",
            "location"
        ]


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Location
        fields = "__all__"
