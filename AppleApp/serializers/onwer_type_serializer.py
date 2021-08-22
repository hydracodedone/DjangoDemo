from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from AppleApp.modelAction.onwer_type_action_set import OwnerTypeModelAction
from AppleApp.util.constant.validate_error import OwnerType_IS_ILLEGAL


def uid_validator(uid_data):
    if not OwnerTypeModelAction.check_uid_is_exsist(uid_data):
        raise ValidationError(OwnerType_IS_ILLEGAL)


class OwnerTypeUidSeriazlier(serializers.Serializer):
    uid = serializers.UUIDField(allow_null=False, validators=[uid_validator])

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class OwnerTypeSerializer(OwnerTypeUidSeriazlier):
    owner_type_name = serializers.CharField(allow_null=False, allow_blank=False)

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")
