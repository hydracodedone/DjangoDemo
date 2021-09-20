from rest_framework import serializers

from AppleApp.models import OwnerType


class OwnerTypeUidSeriazlier(serializers.Serializer):
    owner_type_uid = serializers.PrimaryKeyRelatedField(
        queryset=OwnerType.custom_objects.only("uid"),
        required=True,
    )

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class OwnerTypeSerializer(OwnerTypeUidSeriazlier, serializers.Serializer):
    owner_type_name = serializers.CharField(allow_null=False, allow_blank=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class UserRelatedInfoSerializer(serializers.Serializer):
    owner_type = OwnerTypeSerializer(many=True)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
