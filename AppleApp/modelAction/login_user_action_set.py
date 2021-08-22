from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework.exceptions import ValidationError as DRFValidationError

from AppleApp.modelAction.onwer_type_action_set import OwnerTypeModelAction
from AppleApp.modelAction.owner_action_set import OwnerModelAction
from AppleApp.models import LoginUser


class LoginModelAction(object):
    @staticmethod
    def create_new_user(**validate_data):
        owner_type_uid = validate_data.pop("owner_type")
        instance = LoginUser(**validate_data)
        try:
            instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            with transaction.atomic():
                user_instance = LoginUser.custom_objects.create(**validate_data)
                owner_type_isntance = OwnerTypeModelAction.get_owner_type_instance(owner_type_uid)
                OwnerModelAction.create_new_owner(**{
                    "user": user_instance,
                    "owner_type": owner_type_isntance
                })

    @staticmethod
    def query_all_user_with_owner_info():
        return LoginUser.custom_objects.select_related("owner").prefetch_related("owner__owner_type").all()

    @staticmethod
    def update_user(**validate_data):
        uid = validate_data.pop("uid")
        user_obj = LoginUser.custom_objects.get(uid=uid)
        user_obj.__dict__.update(**validate_data)
        user_obj.__dict__.update({"is_validate": False})
        user_obj.save()
