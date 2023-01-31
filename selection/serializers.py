from rest_framework import serializers

from ads.models import Ad
from ads.serializers import AdDetailSerializer
from selection.models import Selection
from users.models import User


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

    def is_valid(self, *, raise_exception=False):
        self._items = self.initial_data.pop("items")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = Selection.objects.create(**validated_data)

        ad = Ad.objects.get(pk=self._items)
        selection.items.add(ad)

        selection.save()

        return selection


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

    def is_valid(self, *, raise_exception=False):
        self._items = self.initial_data.pop("items", None)
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        selection = super().save()

        if self._items:
            for item in self._items:
                item = Ad.objects.get(pk=item)
                selection.items.add(item)

            selection.save()

        return selection


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]
