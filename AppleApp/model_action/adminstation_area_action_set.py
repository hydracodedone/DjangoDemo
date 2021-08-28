from AppleApp.models import AdministrativeDivision


class AdminstrativeDivisionAction(object):
    @staticmethod
    def __create_single_layar_data(name, code, administrator_type, superial_instance=None):
        instance = AdministrativeDivision.custom_objects.create(
            administrator_name=name,
            administrator_code=code,
            superial_administrator=superial_instance
        )
        if administrator_type == 1:
            instance.is_province = True
        if administrator_type == 2:
            instance.is_city = True
        if administrator_type == 3:
            instance.is_county = True
        if administrator_type == 4:
            instance.is_village = True
        if administrator_type == 5:
            instance.is_country = True
        instance.save()
        return instance

    def __insert_data(self, dict_data: dict, administrator_type, superial_instance=None):
        for key, value in dict_data.items():
            name = key
            code = value.get("code")
            inferior = value.get("data")
            superial_instance_temp = self.__create_single_layar_data(
                name=name,
                code=code,
                administrator_type=administrator_type,
                superial_instance=superial_instance,
            )
            if inferior:
                administrator_type += 1
                self.__insert_data(inferior, administrator_type, superial_instance_temp)

    @staticmethod
    def query_all_administrative_data():
        return AdministrativeDivision.custom_objects.prefetch_related("superial_administrator").filter(
            is_province=True).all()
