from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from AppleApp.models import AppleType, AppleLevel, AppleMaturity, ApplePesticideResidue, ApplePackingType, AppleInstance
from FirstProject.util.constant.validate_error import MODIFY_ILLEGAL, DATA_IS_SOFTED_DELETED
from FirstProject.util.validate_function.validate_function import positive_float_int_validator


class AppleInstanceUidSerializer(serializers.Serializer):
    apple_instance_uid = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=AppleInstance.custom_objects.only("uid"),
        allow_null=False,
        source="uid"
    )

    def validate_uid(self, data):
        if data.is_deleted:
            raise ValidationError(DATA_IS_SOFTED_DELETED.format(data.uid))
        if not data.owner.user_id == self.context.get("user_uid"):
            raise ValidationError(MODIFY_ILLEGAL)
        else:
            return data

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class AppleInstanceOriginalSerializer(serializers.Serializer):
    type = serializers.PrimaryKeyRelatedField(
        queryset=AppleType.custom_objects.only("uid"),
        required=True,
        allow_null=False,
    )
    level = serializers.PrimaryKeyRelatedField(
        queryset=AppleLevel.custom_objects.only("uid"),
        required=True,
        allow_null=False,
    )
    maturity = serializers.PrimaryKeyRelatedField(
        queryset=AppleMaturity.custom_objects.only("uid"),
        required=True,
        allow_null=False,
    )
    pesticide_residue = serializers.PrimaryKeyRelatedField(
        queryset=ApplePesticideResidue.custom_objects.only("uid"),
        required=True,
        allow_null=False,
    )
    packing_type = serializers.PrimaryKeyRelatedField(
        queryset=ApplePackingType.custom_objects.only("uid"),
        required=True,
        allow_null=False,
    )
    batch_name = serializers.CharField(required=False, allow_null=False)
    sum_remaining = serializers.FloatField(validators=[positive_float_int_validator], required=True, allow_null=False)
    price = serializers.FloatField(validators=[positive_float_int_validator], required=True, allow_null=False)
    product_time = serializers.DateField(required=True, allow_null=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class AppleInstanceCreateSerializer(AppleInstanceOriginalSerializer):
    is_available = serializers.BooleanField(required=True, allow_null=False)
    note = serializers.CharField(required=False, allow_null=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class AppleInstanceAppleInfoUpdateSerializer(AppleInstanceUidSerializer):
    is_available = serializers.BooleanField(required=False, allow_null=False)
    note = serializers.CharField(required=False, allow_null=False)
    type = serializers.PrimaryKeyRelatedField(
        queryset=AppleType.custom_objects.only("uid"),
        required=False,
        allow_null=False,
    )
    level = serializers.PrimaryKeyRelatedField(
        queryset=AppleLevel.custom_objects.only("uid"),
        required=False,
        allow_null=False,
    )
    maturity = serializers.PrimaryKeyRelatedField(
        queryset=AppleMaturity.custom_objects.only("uid"),
        required=False,
        allow_null=False,
    )
    pesticide_residue = serializers.PrimaryKeyRelatedField(
        queryset=ApplePesticideResidue.custom_objects.only("uid"),
        required=False,
        allow_null=False,
    )
    packing_type = serializers.PrimaryKeyRelatedField(
        queryset=ApplePackingType.custom_objects.only("uid"),
        required=False,
        allow_null=False,
    )
    batch_name = serializers.CharField(required=False, allow_null=False)
    sum_remaining = serializers.FloatField(validators=[positive_float_int_validator], required=False, allow_null=False)
    price = serializers.FloatField(validators=[positive_float_int_validator], required=False, allow_null=False)
    product_time = serializers.DateField(required=False, allow_null=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class AppleInstanceAppleInfoDeleteSerializer(AppleInstanceUidSerializer):
    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
