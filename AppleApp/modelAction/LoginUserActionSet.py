from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

from AppleApp.models import LoginUser


class LoginModelAction(object):
    @staticmethod
    def create_new_user(**validate_data):
        instance = LoginUser(**validate_data)
        try:
            instance.full_clean()
        except ValidationError as err:
            raise DRFValidationError(err.message_dict)
        else:
            LoginUser.custom_objects.create(**validate_data)
