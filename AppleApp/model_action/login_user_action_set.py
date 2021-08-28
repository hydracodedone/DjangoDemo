from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework.exceptions import ValidationError as DRFValidationError

from AppleApp.model_action.owner_action_set import OwnerModelAction
from AppleApp.model_action.storage_pool_action_set import StoragePoolModelAction
from AppleApp.model_action.storge_type_action_set import StorageTypeModelAction
from AppleApp.models import LoginUser


class LoginModelAction(object):
    @staticmethod
    def create_new_user(**validate_data):
        owner_type_id = validate_data.pop("owner_type").get("uid")
        user_instance = LoginUser(**validate_data)
        try:
            user_instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            with transaction.atomic():
                user_instance.save()
                owner = OwnerModelAction.create_new_owner(
                    **{
                        "user_id": user_instance.uid,
                        "owner_type_id": owner_type_id,
                    })
                StoragePoolModelAction.create_new_self_storage_pool(
                    **{
                        "pool_type_id": StorageTypeModelAction.get_self_storage_pool_type_uid(),
                        "owner_id": owner.uid,
                        "owner_name": user_instance.name,
                        "phone_number": user_instance.phone_number,
                        "location": user_instance.address,
                    }
                )

    @staticmethod
    def update_user(**validate_data):
        uid = validate_data.pop("uid")
        user_instance = LoginUser.custom_objects.get(uid=uid)
        user_instance.__dict__.update(**validate_data)
        user_instance.__dict__.update({"is_validate": False})
        try:
            user_instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            user_instance.save()
