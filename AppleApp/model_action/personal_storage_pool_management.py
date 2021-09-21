from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

from AppleApp.model_action.common_action import CommenAction
from AppleApp.models import StoragePool, StoragePoolProxyModel
from FirstProject.util.constant.constant import STORAGE_PRIVITE, STORAGE_COMMERCIAL
from FirstProject.util.constant.validate_error import MODIFY_ILLEGAL, DATA_ILLEGAL
from FirstProject.util.customized_exception.global_exception import DataInvalidationException


class StoragePoolModelAction(object):
    @staticmethod
    def create_default_self_storage_pool(**validated_data):
        validated_data.update(**{"is_internal_managed": False})
        validated_data.update(**{"pool_name": "default"})
        validated_data.update(**{"is_internal_managed": False})
        storage_pool_instance = StoragePoolProxyModel(
            **validated_data
        )
        try:
            storage_pool_instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            StoragePool.custom_objects.create(**validated_data)

    @staticmethod
    def create_new_storage_pool(user_instance, **validated_data):
        user_name = user_instance.name
        user_phone_number = user_instance.phone_number
        owner_id = user_instance.owner.uid
        is_internal_managed = False
        location = validated_data.get("location")
        pool_type = validated_data.pop("pool_type")
        capacity = validated_data.get("capacity")
        pool_name = validated_data.get("pool_name")
        print(validated_data)
        if pool_type == STORAGE_PRIVITE:
            pass
        elif pool_type == STORAGE_COMMERCIAL:
            pass
        storage_pool_instance = StoragePoolProxyModel(
            pool_name=pool_name,
            pool_type=pool_type,
            location=location,
            owner_id=owner_id,
            owner_name=user_name,
            phone_number=user_phone_number,
            capacity=capacity,
            capacity_remaining=capacity,
            is_internal_managed=is_internal_managed
        )
        try:
            storage_pool_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            storage_pool_instance.save()

    @staticmethod
    def update_storage_pool(user, **validated_data):
        storage_pool_instance = validated_data.pop("uid")
        if not CommenAction.verify_owner_subordination_relation(user.owner.uid, storage_pool_instance):
            raise DataInvalidationException(MODIFY_ILLEGAL)
        if CommenAction.verify_deleted_relation(storage_pool_instance):
            raise DataInvalidationException(DATA_ILLEGAL)
        new_capcity = validated_data.get("capacity")

        if new_capcity:
            remaing_capacity = storage_pool_instance.get("remaing_capacity")
            if remaing_capacity > new_capcity:
                raise DataInvalidationException(DATA_ILLEGAL)

        storage_pool_instance.__dict__.update(**validated_data)
        try:
            storage_pool_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            storage_pool_instance.save()
