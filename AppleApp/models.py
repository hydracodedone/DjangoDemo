# encoding:UTF-8

import datetime
from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.timezone import utc

from AppleApp.util.util import uuid_general


def get_now_time():
    return datetime.utcnow().replace(tzinfo=utc)


class CommonManager(models.Manager):
    def get_queryset(self):
        return super(CommonManager, self).get_queryset().filter(is_deleted=False)


class CommonData(models.Model):
    uid = models.UUIDField(primary_key=True, auto_created=True, db_index=True, default=uuid_general)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(null=False, default=False)
    objects = CommonManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.delete_time = get_now_time()
        self.save()


class LoginUser(CommonData):
    name = models.CharField(null=False, max_length=10, db_index=True)
    phone_number = models.CharField(null=False, max_length=15)
    login_name = models.CharField(null=False, max_length=20)
    login_password = models.CharField(null=False, max_length=200)
    address = models.CharField(null=True, blank=True, max_length=100)

    def save(self, *args, **kwargs):
        self.login_password = make_password(self.login_password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.login_name

    class Meta:
        db_table = "Login_User"
        unique_together = ["is_deleted", "login_name"]


class OwnerType(CommonData):
    owner_name = models.CharField(null=False, blank=False, unique=True, max_length=20)

    def __str__(self):
        return self.owner_name

    class Meta:
        db_table = "Owner_Type"


class Owner(CommonData):
    owner_type = models.ForeignKey(OwnerType, on_delete=models.CASCADE)
    user = models.OneToOneField(LoginUser, on_delete=models.CASCADE)

    def __str__(self):
        return "[{}]:Name:{}".format(self.owner_type.owner_name, self.user.name)

    class Meta:
        db_table = "Owner"


class StoragePoolType(CommonData):
    pool_type = models.CharField(null=False, unique=True, max_length=20)

    def __str__(self):
        return self.pool_type

    class Meta:
        db_table = "Storage_Pool_Type"


class StoragePool(CommonData):
    pool_type = models.ForeignKey(StoragePoolType, on_delete=models.CASCADE)
    longtitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=200)
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=True)
    phone_number = models.CharField(null=True, blank=True, max_length=11)
    capacity = models.FloatField(null=True, blank=True)
    is_internal_managed = models.BooleanField(null=False, default=True)

    def __str__(self):
        return "[{}]-[{}]".format(self.pool_type, self.owner)

    class Meta:
        db_table = "Storage_Pool"
        unique_together = ["owner", "location"]


class AppleType(CommonData):
    type_name = models.CharField(null=False, blank=False, unique=True, max_length=20)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = "Apple_Type"


class AppleLevel(CommonData):
    level_name = models.CharField(null=False, blank=False, unique=True, max_length=20)

    def __str__(self):
        return self.level_name

    class Meta:
        db_table = "Apple_Level"


class AppleMaturity(CommonData):
    maturity_name = models.CharField(null=False, blank=False, unique=True, max_length=20)

    def __str__(self):
        return self.maturity_name

    class Meta:
        db_table = "Apple_Maturity"


class ApplePesticideResidue(CommonData):
    pesticide_residue_name = models.CharField(null=False, blank=False, unique=True, max_length=20)

    def __str__(self):
        return self.pesticide_residue_name

    class Meta:
        db_table = "Apple_Pesticide_Residue"


class ApplePackingType(CommonData):
    packing_type_name = models.CharField(null=False, blank=False, unique=True, max_length=20)

    def __str__(self):
        return self.packing_type_name

    class Meta:
        db_table = "Apple_Packing_Type"


class AppleInstance(CommonData):
    batch_name = models.CharField(null=True, max_length=30)
    type = models.ForeignKey(AppleType, related_name="apple", on_delete=models.CASCADE)
    level = models.ForeignKey(AppleLevel, related_name="apple", on_delete=models.CASCADE)
    maturity = models.ForeignKey(AppleMaturity, related_name="apple", on_delete=models.CASCADE)
    pesticide_residue = models.ForeignKey(ApplePesticideResidue, related_name="apple", on_delete=models.CASCADE)
    packing_type = models.ForeignKey(ApplePackingType, related_name="apple", on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    storage = models.ManyToManyField(StoragePool, through='AppleInstanceThroughStorage')

    sum_remaining = models.FloatField(null=False)
    price = models.FloatField(null=True, blank=True)
    product_time = models.DateField(null=False)
    is_available = models.BooleanField(null=False, default=True)
    note = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return "[{}]-[{}]-[{}]-[{}]-[{}]".format(
            self.type.type_name,
            self.level.level_name,
            self.maturity.maturity_name,
            self.sum_remaining,
            self.price
        )

    class Meta:
        db_table = "Apple_Instance"


class AppleInstanceThroughStorage(CommonData):
    storage_pool = models.ForeignKey(StoragePool, on_delete=models.CASCADE)
    apple_instance = models.ForeignKey(AppleInstance, on_delete=models.CASCADE)
    remaining = models.FloatField(null=False)
    incoming_time = models.DateField()
    note = models.CharField(null=True, blank=True, max_length=300)

    class Meta:
        db_table = "Apple_Instance_Through_Storage"

    def __str__(self):
        return "[{}]-[{}]".format(self.apple_instance.owner, self.remaining)


class StoragePoolQuantityChangeLogType(CommonData):
    change_type = models.CharField(null=False, unique=True, max_length=10)

    def __str__(self):
        return self.change_type

    class Meta:
        db_table = "Storage_Pool_Quantity_ChangeLog_Type"


class StoragePoolQuantityChangeLog(CommonData):
    record_type = models.ForeignKey(StoragePoolQuantityChangeLogType, on_delete=models.CASCADE)
    storage = models.ForeignKey(AppleInstanceThroughStorage, on_delete=models.CASCADE)
    change_number = models.FloatField(null=False)
    remaining = models.FloatField(null=False)
    note = models.CharField(null=True, blank=True, max_length=300)

    class Meta:
        db_table = "Storage_Pool_Quantity_ChangeLog"
