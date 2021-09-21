class CommenAction(object):
    @staticmethod
    def verify_user_subordination_relation(user_uid, instance):
        if instance.user.uid == user_uid:
            return True
        else:
            return False

    @staticmethod
    def verify_owner_subordination_relation(owner_uid, instance):
        if instance.owner.uid == owner_uid:
            return True
        else:
            return False

    @staticmethod
    def verify_deleted_relation(instance):
        if instance.is_deleted:
            return False
        else:
            return True
