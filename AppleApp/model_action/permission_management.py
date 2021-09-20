from AppleApp.models import LoginUser


class PermissionActionSet(object):
    @staticmethod
    def get_specific_permission(user_instance: LoginUser):
        permission_list = list()
        permissions_group = user_instance.permission_groups.all()
        for each_group in permissions_group:
            permission = each_group.permissions_detail.only("url").all().values("url")
            permission_list.extend([temp.get("url") for temp in permission])
        return set(permission_list)
