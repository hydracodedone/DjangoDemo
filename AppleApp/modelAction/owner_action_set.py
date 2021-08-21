from AppleApp.models import Owner


class OwnerModelAction(object):
    @staticmethod
    def create_new_owner(**validate_data):
        user_instance = validate_data.get("user")
        owner_type_instance = validate_data.get("owner_type")
        return Owner.custom_objects.create(user=user_instance, owner_type=owner_type_instance)
