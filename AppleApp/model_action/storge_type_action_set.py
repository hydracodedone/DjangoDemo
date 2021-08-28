from AppleApp.models import StoragePoolType


class StorageTypeModelAction(object):
    @staticmethod
    def get_all_data():
        return StoragePoolType.custom_objects.all()

    @staticmethod
    def get_self_storage_pool_type_uid():
        return StoragePoolType.custom_objects.first().uid
