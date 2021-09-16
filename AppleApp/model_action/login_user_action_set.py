from django.core.exceptions import ValidationError
from django.db import transaction

from AppleApp.model_action.owner_action_set import OwnerModelAction
from AppleApp.model_action.storage_pool_action_set import StoragePoolModelAction
from AppleApp.model_action.storge_type_action_set import StorageTypeModelAction
from AppleApp.models import LoginUser
from FirstProject.util.constant.model_action_error import LOGIN_FAIL
from FirstProject.util.customized_exception.global_exception import DataInvalidationException


class LoginModelAction(object):
    @staticmethod
    def create_new_user(**validate_data):
        owner_type_id = validate_data.pop("owner_type").get("uid")
        user_instance = LoginUser(**validate_data)
        try:
            user_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            with transaction.atomic():
                user_instance = LoginUser.custom_objects.create(**validate_data)
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
        user_instance = LoginUser.custom_objects.filter(uid=uid).first()
        user_instance.__dict__.update(**validate_data)
        user_instance.__dict__.update({"is_validate": False})
        try:
            user_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            user_instance.save()

    @staticmethod
    def query_user_by_uid(uid):
        if LoginUser.custom_objects.filter(uid=uid).first():
            return True
        else:
            return False

    @staticmethod
    def query_user_by_login_user_name_and_password(**validated_data):
        login_name = validated_data.get("login_name")
        login_password = validated_data.get("login_password")
        user_instance = LoginUser.custom_objects.filter(
            login_name=login_name,
            login_password=login_password
        ).only("uid", "login_name").first()
        if not user_instance:
            raise DataInvalidationException(
                {"invalid input": LOGIN_FAIL}
            )
        else:
            return user_instance

    @staticmethod
    def query_user_by_uid_and_user_name(**validate_data):
        uid = validate_data.get("uid")
        login_name = validate_data.get("login_name")
        return LoginUser.custom_objects.filter(
            login_name=login_name,
            uid=uid
        ).first()
