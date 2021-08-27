from rest_framework import serializers


class AppleInstanceAppleInfoReadSerializer(serializers.Serializer):
    type = serializers.StringRelatedField(read_only=True)
    level = serializers.StringRelatedField(read_only=True)
    maturity = serializers.StringRelatedField(read_only=True)
    pesticide_residue = serializers.StringRelatedField(read_only=True)
    packing_type = serializers.StringRelatedField(read_only=True)
    batch_name = serializers.CharField(read_only=True)
    sum_remaining = serializers.FloatField(read_only=True)
    price = serializers.FloatField(read_only=True)
    product_time = serializers.DateField(read_only=True)
    is_available = serializers.BooleanField(read_only=True)
    note = serializers.CharField(read_only=True)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

