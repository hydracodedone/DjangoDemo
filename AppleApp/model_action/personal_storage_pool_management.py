from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

from AppleApp.models import StoragePool


class StoragePoolModelAction(object):
    @staticmethod
    def create_new_self_storage_pool(**validated_data):
        validated_data.update(**{"is_internal_managed": False})
        storage_pool_instance = StoragePool(
            **validated_data
        )
        try:
            storage_pool_instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            StoragePool.custom_objects.create(**validated_data)
