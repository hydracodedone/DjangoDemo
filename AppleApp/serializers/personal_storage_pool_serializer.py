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


class StoragePoolOriginalSerializer(serializers.Serializer):
    pool_type = serializers.ChoiceField(
        required=True,
        choices=StoragePool.pool_type_choice,
    )
    location = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    capacity = serializers.FloatField(required=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class StoragePoolCreateSerializer(StoragePoolOriginalSerializer):
    note = serializers.CharField(required=False, allow_null=True, allow_blank=False)
    pool_name = serializers.CharField(required=True, allow_null=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class StoragePoolUpdateSerializer(StoragePoolUidSerializer, serializers.Serializer):
    location = serializers.CharField(required=False, allow_null=False, allow_blank=False)
    capacity = serializers.FloatField(required=False)
    note = serializers.CharField(required=False, allow_null=True, allow_blank=False)
    pool_name = serializers.CharField(required=False, allow_null=False)
    phone_number = serializers.CharField(required=False, allow_null=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
