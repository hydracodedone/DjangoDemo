from rest_framework import serializers


class AdministrativeDivisionSerializer(serializers.Serializer):
    administrator_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    administrator_code = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    inferior = serializers.SerializerMethodField()

    def get_inferior(self, data):
        inferior_data = data.administrativedivision_set.all()
        if inferior_data:
            return AdministrativeDivisionSerializer(inferior_data, many=True).data
        else:
            return []

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
