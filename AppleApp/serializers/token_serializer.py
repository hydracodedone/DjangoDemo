from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(allow_null=False, allow_blank=False, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
