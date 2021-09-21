from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import transaction

from AppleApp.model_action.owner_management import OwnerModelAction
from AppleApp.model_action.personal_storage_pool_management import StoragePoolModelAction
from AppleApp.models import LoginUser
from FirstProject.util.constant.constant import STORAGE_PRIVITE
from FirstProject.util.constant.model_action_error import LOGIN_FAIL
from FirstProject.util.customized_exception.global_exception import DataInvalidationException


class LoginModelAction(object):
    @staticmethod
    def create_new_user(**validated_data):
        owner_type_uid = validated_data.pop("owner_type_uid").uid
        user_instance = LoginUser(**validated_data)
        try:
            user_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            with transaction.atomic():
                validated_data.update(**{"is_validate": False})
                user_instance = LoginUser.custom_objects.create(**validated_data)
                owner = OwnerModelAction.create_new_owner(
                    **{
                        "user_id": user_instance.uid,
                        "owner_type_uid": owner_type_uid,
                    })
                StoragePoolModelAction.create_default_self_storage_pool(
                    **{
                        "pool_type": STORAGE_PRIVITE,
                        "owner_id": owner.uid,
                        "owner_name": user_instance.name,
                        "phone_number": user_instance.phone_number,
                        "location": user_instance.address,
                    }
                )

    @staticmethod
    def update_user(**validated_data):
        uid = validated_data.pop("uid")
        login_password = validated_data.get("login_password", None)
        if login_password:
            validated_data["login_password"] = make_password(login_password, settings.PASSWORD_SALT, "pbkdf2_sha256")
        user_instance = LoginUser.custom_objects.filter(uid=uid).first()
        user_instance.__dict__.update(**validated_data)
        user_instance.__dict__.update({"is_validate": False})
        try:
            user_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            user_instance.save()

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
    def query_user_by_uid_and_user_name(**validated_data):
        uid = validated_data.get("uid")
        login_name = validated_data.get("login_name")
        return LoginUser.custom_objects.filter(
            login_name=login_name,
            uid=uid
        ).first()
