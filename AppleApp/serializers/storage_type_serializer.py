from rest_framework import serializers


class StorageTypeSerializer(serializers.Serializer):
    uid = serializers.UUIDField(allow_null=False)
    pool_type = serializers.CharField(allow_null=False, allow_blank=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
