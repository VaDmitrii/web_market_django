from rest_framework import serializers

from users.models import User, Location


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
