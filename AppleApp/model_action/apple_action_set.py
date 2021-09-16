from django.core.exceptions import ValidationError

from AppleApp.models import AppleInstance
from FirstProject.util.customized_exception.global_exception import DataInvalidationException


class AppleModelAction(object):

    @staticmethod
    def create_new_batch_apple(**validated_data):
        apple_instance = AppleInstance(**validated_data)
        try:
            apple_instance.full_clean()
        except ValidationError as err:
            raise DataInvalidationException(err.message_dict)
        else:
            apple_instance.save()
