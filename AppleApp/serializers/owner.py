from rest_framework import serializers

from AppleApp.models import Owner


class OwnerPhoneNumberReadMixInField(serializers.Field):

    def to_representation(self, data):
        return data.phone_number

    def to_internal_value(self, value):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class OwnerNameReadFMixInField(serializers.Field):

    def to_representation(self, data):
        return data.name

    def to_internal_value(self, value):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class OwnerReadSerializer(serializers.ModelSerializer):
    owner_type = serializers.StringRelatedField(read_only=True, many=False)
    owner_phone = OwnerPhoneNumberReadMixInField(source="user")
    owner_name = OwnerNameReadFMixInField(source="user")

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    class Meta:
        model = Owner
        fields = ["owner_type", "owner_phone", "owner_name"]


class OwnerInfoForeignKeyReadSerializer(serializers.Serializer):
    owner = OwnerReadSerializer(read_only=True, many=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
