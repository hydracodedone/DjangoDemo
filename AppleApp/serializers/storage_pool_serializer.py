from rest_framework import serializers

from AppleApp.models import StoragePool


class StoragePoolUidSerializer(serializers.Serializer):
    storage_pool_uid = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=StoragePool.custom_objects.only("uid"),
        allow_null=False,
        source="uid"
    )

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class StoragePoolInfoSerializer(StoragePoolUidSerializer):
    pool_type = serializers.StringRelatedField(read_only=True)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
