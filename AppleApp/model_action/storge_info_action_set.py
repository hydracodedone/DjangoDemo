from AppleApp.models import StoragePoolType, StoragePoolQuantityChangeLogType


class StorageTypeModelAction(object):

    @staticmethod
    def get_self_storage_pool_type_uid():
        return StoragePoolType.custom_objects.first().uid

    @staticmethod
    def get_storage_info():
        return {
            "storage_pool_type": StoragePoolType.custom_objects.all(),
            "storage_log_type": StoragePoolQuantityChangeLogType.custom_objects.all()
        }
