from rest_framework import serializers


class AppleTypeSerializer(serializers.Serializer):
    apple_type_uid = serializers.PrimaryKeyRelatedField(read_only=True, source="uid")
    name = serializers.CharField(source="type_name")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AppleLevelSerializer(serializers.Serializer):
    apple_level_uid = serializers.PrimaryKeyRelatedField(read_only=True, source="uid")
    name = serializers.CharField(source="level_name")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AppleMaturitySerializer(serializers.Serializer):
    apple_maturity_uid = serializers.PrimaryKeyRelatedField(read_only=True, source="uid")
    name = serializers.CharField(source="maturity_name")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ApplePesticideResidueSerializer(serializers.Serializer):
    apple_pesticde_residue_uid = serializers.PrimaryKeyRelatedField(read_only=True, source="uid")
    name = serializers.CharField(source="pesticide_residue_name")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ApplePackingTypeSerializer(serializers.Serializer):
    apple_packing_type_uid = serializers.PrimaryKeyRelatedField(read_only=True, source="uid")
    name = serializers.CharField(source="packing_type_name")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AppleFeatureSerializer(serializers.Serializer):
    apple_type = AppleTypeSerializer(many=True)
    apple_level = AppleLevelSerializer(many=True)
    apple_maturity = AppleMaturitySerializer(many=True)
    apple_pesticide_residue = ApplePesticideResidueSerializer(many=True)
    apple_packing_type = ApplePackingTypeSerializer(many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
