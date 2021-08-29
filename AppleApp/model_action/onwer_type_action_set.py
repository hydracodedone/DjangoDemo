from AppleApp.models import OwnerType


class OwnerTypeModelAction(object):
    @staticmethod
    def check_uid_is_exsist(uid_data):
        return OwnerType.custom_objects.filter(uid=uid_data).exists()

    @staticmethod
    def get_all_data():
        return OwnerType.custom_objects.all()
