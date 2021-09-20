from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

from AppleApp.models import Owner


class OwnerModelAction(object):
    @staticmethod
    def create_new_owner(**validate_data):
        user_id = validate_data.get("user_id")
        owner_type_id = validate_data.get("owner_type_uid")
        owner_instance = Owner(user_id=user_id, owner_type_id=owner_type_id)
        try:
            owner_instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            owner_instance.save()
            return owner_instance
