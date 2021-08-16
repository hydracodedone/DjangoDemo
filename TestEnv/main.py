import os

import django

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FirstProject.settings")
    django.setup()

    from AppleApp.models import *

    userObj = LoginUser.custom_objects.last()
    ownerTypeObj = OwnerType.custom_objects.last()
    Owner.custom_objects.create(user=userObj, owner_type=ownerTypeObj)
