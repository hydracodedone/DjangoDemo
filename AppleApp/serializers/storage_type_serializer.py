from rest_framework import serializers


class StorageTypeSerializer(serializers.Serializer):
    storage_type_uid = serializers.PrimaryKeyRelatedField(read_only=True, source="uid")
    pool_type = serializers.CharField(allow_null=False, allow_blank=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class StorageLogTypeSerializer(serializers.Serializer):
    storage_log_type_uid = serializers.PrimaryKeyRelatedField(read_only=True, source="uid")
    change_type = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    add_or_sub = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        source="get_add_or_sub_display"
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class StorageRelatedInfoSerializer(serializers.Serializer):
    storage_pool_type = StorageTypeSerializer(many=True)
    storage_log_type = StorageLogTypeSerializer(many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
