from rest_framework import serializers

from AppleApp.models import StoragePoolQuantityChangeLogType


class StorageChangeLogTypeSerializer(serializers.Serializer):
    change_log_type = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=StoragePoolQuantityChangeLogType.custom_objects.only("uid"),
        allow_null=False
    )

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
