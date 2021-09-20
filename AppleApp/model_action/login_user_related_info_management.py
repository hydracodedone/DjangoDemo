from AppleApp.models import OwnerType


class OwnerTypeModelAction(object):
    @staticmethod
    def get_all_data():
        return OwnerType.custom_objects.all()


class LoginUserRelatedAction(object):
    @staticmethod
    def query_login_user_related_info():
        return {
            "owner_type": OwnerTypeModelAction.get_all_data()
        }
