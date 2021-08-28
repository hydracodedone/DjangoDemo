from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

from AppleApp.models import StoragePool


class StoragePoolModelAction(object):
    @staticmethod
    def create_new_self_storage_pool(**validated_data):
        pool_type_id = validated_data.get("pool_type_id")
        owner_id = validated_data.get("owner_id")
        owner_name = validated_data.get("owner_name")
        phone_number = validated_data.get("phone_number")
        location = validated_data.get("location")
        storage_pool_instance = StoragePool(
            pool_type_id=pool_type_id,
            owner_id=owner_id,
            owner_name=owner_name,
            phone_number=phone_number,
            location=location,
            is_internal_managed=False
        )
        try:
            storage_pool_instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            storage_pool_instance.save()
