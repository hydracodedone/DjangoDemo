from AppleApp.models import StoragePool, StoragePoolQuantityChangeLog


class StoragePoolRelatedInfoManagement(object):
    def query_data(self):
        return {
            "storage_pool_type": self.__generate_storage_pool_type(),
            "storage_pool_log_type": self.__generate_storage_log_type()
        }

    @staticmethod
    def __generate_storage_pool_type():
        result = []
        for each in StoragePool.pool_type_choice:
            result.append(
                {
                    "storage_pool_value": each[0],
                    "storage_pool_name": each[1],
                }
            )
        return result

    @staticmethod
    def __generate_storage_log_type():
        result = []
        for each in StoragePoolQuantityChangeLog.change_choice:
            result.append(
                {
                    "storage_pool_log_type_value": each[0],
                    "storage_pool_log_type_name": each[1],
                }
            )
        return result
