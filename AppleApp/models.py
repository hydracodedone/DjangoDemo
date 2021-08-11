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
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后一次更新时间")
    delete_time = models.DateTimeField(null=True, blank=True, verbose_name="删除时间")
    is_deleted = models.BooleanField(null=False, default=False, verbose_name="是否删除")
    objects = CommonManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.delete_time = get_now_time()
        self.save()


class LoginUser(CommonData):
    name = models.CharField(null=False, blank=False, max_length=10, db_index=True, verbose_name="姓名")
    phone_number = models.CharField(null=False, blank=False, max_length=15, verbose_name="联系电话")
    login_name = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="登陆用户名")
    login_password = models.CharField(null=False, blank=False, max_length=200, verbose_name="密码")
    address = models.CharField(null=True, blank=True, max_length=100, verbose_name="地址")
    is_validate = models.BooleanField(null=False, blank=False, default=False, verbose_name="人工是否审核")

    def save(self, *args, **kwargs):
        self.login_password = make_password(self.login_password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.login_name

    class Meta:
        db_table = "Login_User"
        unique_together = ["is_deleted", "login_name"]
        verbose_name_plural = "注册用户"


class OwnerType(CommonData):
    owner_name = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="商家类型")

    def __str__(self):
        return self.owner_name

    class Meta:
        db_table = "Owner_Type"
        verbose_name_plural = "商家类型"


class Owner(CommonData):
    owner_type = models.ForeignKey(OwnerType, null=False, blank=False, on_delete=models.CASCADE, verbose_name="商家类型")
    user = models.OneToOneField(LoginUser, null=False, blank=False, on_delete=models.CASCADE, verbose_name="对应的注册用户")

    def __str__(self):
        return "商家类型:{},用户姓名:{}".format(self.owner_type.owner_name, self.user.name)

    class Meta:
        db_table = "Owner"
        verbose_name_plural = "商家"


class StoragePoolType(CommonData):
    pool_type = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="仓库类型")

    def __str__(self):
        return self.pool_type

    class Meta:
        db_table = "Storage_Pool_Type"
        verbose_name_plural = "仓库类型"


class StoragePool(CommonData):
    pool_type = models.ForeignKey(StoragePoolType, null=False, blank=False, on_delete=models.CASCADE,
                                  verbose_name="仓库类型")
    longtitude = models.FloatField(null=True, blank=True, verbose_name="经度")
    latitude = models.FloatField(null=True, blank=True, verbose_name="纬度")
    location = models.CharField(null=False, blank=False, max_length=200, verbose_name="仓库详细地址")
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=True, verbose_name="仓库法人")
    phone_number = models.CharField(null=False, blank=False, max_length=11, verbose_name="仓库联系电话")
    capacity = models.FloatField(null=True, blank=True, verbose_name="仓库总容量")
    is_internal_managed = models.BooleanField(null=False, blank=False, default=True, verbose_name="是否为内部维护信息")

    def __str__(self):
        return "[{}]-[{}]".format(self.pool_type, self.owner)

    class Meta:
        db_table = "Storage_Pool"
        unique_together = ["owner", "location", "phone_number"]
        verbose_name_plural = "仓库"


class AppleType(CommonData):
    type_name = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="苹果种类")

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = "Apple_Type"
        verbose_name_plural = "苹果种类"


class AppleLevel(CommonData):
    level_name = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="苹果等级")

    def __str__(self):
        return self.level_name

    class Meta:
        db_table = "Apple_Level"
        verbose_name_plural = "苹果等级"


class AppleMaturity(CommonData):
    maturity_name = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="苹果成熟度")

    def __str__(self):
        return self.maturity_name

    class Meta:
        db_table = "Apple_Maturity"
        verbose_name_plural = "苹果成熟度"


class ApplePesticideResidue(CommonData):
    pesticide_residue_name = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="农药残留量")

    def __str__(self):
        return self.pesticide_residue_name

    class Meta:
        db_table = "Apple_Pesticide_Residue"
        verbose_name_plural = "苹果农药残留量"


class ApplePackingType(CommonData):
    packing_type_name = models.CharField(null=False, blank=False, unique=True, max_length=20, verbose_name="包装方式")

    def __str__(self):
        return self.packing_type_name

    class Meta:
        db_table = "Apple_Packing_Type"
        verbose_name_plural = "苹果包装方式"


class AppleInstance(CommonData):
    batch_name = models.CharField(null=True, blank=True, max_length=30, verbose_name="苹果批次名称")
    type = models.ForeignKey(AppleType, related_name="apple", null=False, blank=False, on_delete=models.CASCADE,
                             verbose_name="苹果类型")
    level = models.ForeignKey(AppleLevel, related_name="apple", null=False, blank=False, on_delete=models.CASCADE,
                              verbose_name="苹果等级")
    maturity = models.ForeignKey(AppleMaturity, related_name="apple", null=False, blank=False, on_delete=models.CASCADE,
                                 verbose_name="苹果成熟度")
    pesticide_residue = models.ForeignKey(ApplePesticideResidue, related_name="apple", null=False, blank=False,
                                          on_delete=models.CASCADE, verbose_name="农药残留量")
    packing_type = models.ForeignKey(ApplePackingType, related_name="apple", null=False, blank=False,
                                     on_delete=models.CASCADE, verbose_name="苹果包装方式")
    owner = models.ForeignKey(Owner, null=False, blank=False, on_delete=models.CASCADE, verbose_name="苹果所有者")

    storage = models.ManyToManyField(StoragePool, through='AppleInstanceThroughStorage', verbose_name="苹果存储地点")

    sum_remaining = models.FloatField(null=False, blank=False, verbose_name="该批次苹果现存总量")
    price = models.FloatField(null=False, blank=False, verbose_name="预期售出价格")
    product_time = models.DateField(null=False, verbose_name="苹果生产日期")
    is_available = models.BooleanField(null=False, blank=False, default=True, verbose_name="是否愿意出售")
    is_empty = models.BooleanField(null=False, blank=False, default=True, verbose_name="是否售空")
    note = models.CharField(null=True, blank=True, max_length=300, verbose_name="备注")

    def __str__(self):
        return "苹果类型:{},苹果等级:{},苹果总量:{},苹果预期价格:{}".format(
            self.type.type_name,
            self.level.level_name,
            self.sum_remaining,
            self.price
        )

    class Meta:
        db_table = "Apple_Instance"
        verbose_name_plural = "苹果批次信息"


class AppleInstanceThroughStorage(CommonData):
    storage_pool = models.ForeignKey(StoragePool, null=False, blank=False, on_delete=models.CASCADE,
                                     verbose_name="苹果保存仓库")
    apple_instance = models.ForeignKey(AppleInstance, null=False, blank=False, on_delete=models.CASCADE,
                                       verbose_name="苹果批次信息")
    remaining = models.FloatField(null=False, blank=False, verbose_name="现余存量")
    incoming_time = models.DateField(null=False, blank=False, verbose_name="入库时间")
    note = models.CharField(null=True, blank=True, max_length=300)
    is_available = models.BooleanField(null=False, blank=False, default=True, verbose_name="是否愿意出售")
    is_empty = models.BooleanField(null=False, blank=False, default=True, verbose_name="是否售空")

    def __str__(self) -> str:
        return "苹果批次:{},现余存量:{},".format(self.apple_instance.owner, self.remaining)

    class Meta:
        db_table = "Apple_Instance_Through_Storage"
        verbose_name_plural = "苹果库存信息"


class StoragePoolQuantityChangeLogType(CommonData):
    change_type = models.CharField(null=False, blank=False, unique=True, max_length=10, verbose_name="账目类型")

    def __str__(self):
        return self.change_type

    class Meta:
        db_table = "Storage_Pool_Quantity_ChangeLog_Type"
        verbose_name_plural = "账目类型"


class StoragePoolQuantityChangeLog(CommonData):
    record_type = models.ForeignKey(StoragePoolQuantityChangeLogType, null=False, blank=False, on_delete=models.CASCADE,
                                    verbose_name="账目类型")
    storage = models.ForeignKey(AppleInstanceThroughStorage, null=False, blank=False, on_delete=models.CASCADE,
                                verbose_name="对应仓库")
    change_number = models.FloatField(null=False, blank=False, verbose_name="变更数量")
    remaining = models.FloatField(null=False, blank=False, verbose_name="本次变更后剩余数量")
    is_empty = models.BooleanField(null=False, blank=False, default=True, verbose_name="是否售空")
    note = models.CharField(null=True, blank=True, max_length=300, verbose_name="备注")

    class Meta:
        db_table = "Storage_Pool_Quantity_ChangeLog"
        verbose_name_plural = "账目流水"
