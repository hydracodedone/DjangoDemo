from rest_framework import serializers


class StorageInfoReadSerializer(serializers.Serializer):
    pool_type = serializers.StringRelatedField(read_only=True)
    location = serializers.CharField(read_only=True, allow_null=True, allow_blank=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class StorageInfoForeignKeyReadSerializer(serializers.Serializer):
    storage = StorageInfoReadSerializer(read_only=True, many=True)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
