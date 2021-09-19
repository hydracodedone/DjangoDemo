from django.core.exceptions import ValidationError

from AppleApp.models import AppleInstance
from FirstProject.util.customized_exception.global_exception import DataInvalidationException


class AppleModelAction(object):

    @staticmethod
    def create_new_apple_storage_info(**validated_data):
        apple_instance = AppleInstance(**validated_data)
        try:
            apple_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            apple_instance.save()

    @staticmethod
    def update_new_apple_storage_info(**validated_data):
        apple_instance = validated_data.pop("uid")
        for key, value in validated_data.items():
            if not hasattr(apple_instance, key):
                raise DataInvalidationException("illegal operation")
            else:
                setattr(apple_instance, key, value)
        try:
            apple_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            apple_instance.save()

    @staticmethod
    def delete_apple_storage_info(**validated_data):
        apple_instance = validated_data.pop("uid")
        apple_instance_uid = apple_instance.uid
        AppleInstance.custom_objects.filter(uid=apple_instance_uid).first().delete()
