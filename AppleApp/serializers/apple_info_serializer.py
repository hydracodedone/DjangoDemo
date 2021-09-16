from rest_framework import serializers

from AppleApp.models import AppleType, AppleLevel, AppleMaturity, ApplePesticideResidue, ApplePackingType
from FirstProject.util.validate_function.validate_function import positive_float_int_validator


class AppleInstanceAppleInfoOriginalSerializer(serializers.Serializer):
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


class AppleInstanceAppleInfoWriteSerializer(AppleInstanceAppleInfoOriginalSerializer):
    is_available = serializers.BooleanField(required=True, allow_null=False)
    note = serializers.CharField(required=False, allow_null=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
