from django.core.exceptions import ValidationError

from AppleApp.model_action.common_action import CommenAction
from AppleApp.models import AppleInstance
from FirstProject.util.constant.validate_error import MODIFY_ILLEGAL, DATA_ILLEGAL
from FirstProject.util.customized_exception.global_exception import DataInvalidationException


class AppleModelAction(object):

    @staticmethod
    def create_new_batch_apple(**validated_data):
        validated_data.update(**{"is_empty": False})
        apple_instance = AppleInstance(**validated_data)
        try:
            apple_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            AppleInstance.custom_objects.create(**validated_data)

    @staticmethod
    def update_apple_info(user, **validated_data):
        apple_instance = validated_data.pop("uid")
        if not CommenAction.verify_owner_subordination_relation(user.owner.uid, apple_instance):
            raise DataInvalidationException(MODIFY_ILLEGAL)
        if CommenAction.verify_deleted_relation(apple_instance):
            raise DataInvalidationException(DATA_ILLEGAL)
        apple_instance.__dict__.update(**validated_data)
        try:
            apple_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            apple_instance.save()

    # todo
    @staticmethod
    def delete_apple_info(**validated_data):
        apple_instance = validated_data.pop("uid")
        apple_instance_uid = apple_instance.uid
        AppleInstance.custom_objects.filter(uid=apple_instance_uid).first().delete()

    # todo
    @staticmethod
    def query_apple_info(owner_uid):
        return AppleInstance.custom_objects.filter(owner_id=owner_uid)
