from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    msg = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    err = serializers.CharField(required=True, allow_null=False, allow_blank=False)
