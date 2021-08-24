# encoding:UTF-8
# todo Rebuild
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models import FloatField, Sum
from django.utils.safestring import mark_safe

from AppleApp.models import LoginUser, OwnerType, Owner, AppleType, AppleLevel, AppleMaturity, ApplePesticideResidue, \
    ApplePackingType, AppleInstance, StoragePoolType, StoragePool, AppleInstanceThroughStorage, \
    StoragePoolQuantityChangeLogType, StoragePoolQuantityChangeLog


class AdminAbstract(ModelAdmin):
    actions_selection_counter = True
    date_hierarchy = "create_time"
    empty_value_display = "暂无数据"
    list_max_show_all = 100
    preserve_filters = True
    list_select_related = True
    show_full_result_count = False
    actions_on_top = True


@admin.register(LoginUser)
class AdminLoginUser(AdminAbstract):
    list_display = ["name", "phone_number", "login_name", "address", "is_validate"]
    list_editable = ["name", "phone_number", "login_name", "address", "is_validate"]
    search_fields = ["name", "phone_number", "login_name"]
    list_display_links = None
    list_filter = ["is_validate"]


@admin.register(OwnerType)
class AdminOwnerType(AdminAbstract):
    pass


@admin.register(Owner)
class AdminOwner(AdminAbstract):
    class AppleInstanceInlineModel(admin.TabularInline):
        extra = 1
        model = AppleInstance

    def get_apple_sum_remaining(self, obj):
        return obj.appleinstance_set.all().aggregate(
            Sum(
                "sum_remaining",
                output_field=FloatField()
            )
        ).get("sum_remaining__sum")

    def get_apple_avaliable_remaining(self, obj):
        return obj.appleinstance_set.filter(is_available=True).all().aggregate(
            Sum(
                "sum_remaining",
                output_field=FloatField()
            )
        ).get("sum_remaining__sum")

    def apple_detail_button(self, obj):
        button = "<a class ='icon fa fa-detail' style='color: violet' href='/admin/AppleApp/appleinstance/?q={}'>detail</a>".format(
            obj.user.uid.hex)

        return mark_safe(button)

    def get_name(self, obj):
        return obj.user.name

    get_name.short_description = "商户名称"
    apple_detail_button.short_description = "苹果详情"
    get_apple_avaliable_remaining.short_description = "商户现拥有可出售苹果总量"
    get_apple_sum_remaining.short_description = "商户现拥有苹果总量"

    apple_detail_button.allow_tags = True

    list_filter = ["owner_type"]
    search_fields = ["user__uid", "user__name", "user__phone_number"]
    list_select_related = ["user"]
    list_display = ["get_name", "owner_type", "get_apple_sum_remaining", "get_apple_avaliable_remaining",
                    "apple_detail_button"]
    inlines = [AppleInstanceInlineModel]


@admin.register(AppleType)
class AdminAppleType(AdminAbstract):
    pass


@admin.register(AppleLevel)
class AdminAppleLevel(AdminAbstract):
    pass


@admin.register(AppleMaturity)
class AdminAppleMaturity(AdminAbstract):
    pass


@admin.register(ApplePesticideResidue)
class AdminApplePesticideResidue(AdminAbstract):
    pass


@admin.register(ApplePackingType)
class AdminApplePackingType(AdminAbstract):
    pass


@admin.register(AppleInstance)
class AdminAppleInstance(AdminAbstract):

    def get_owner_type(self, obj):
        return obj.owner.owner_type.owner_type_name

    def get_user_phone(self, obj):
        return obj.owner.user.phone_number

    def get_owner_info(self, obj):
        owner_button = "<a class ='icon fa fa-detail' style='color: violet' href='/admin/AppleApp/owner/?q={}'>{}</a>".format(
            obj.owner.user.uid.hex,
            obj.owner.user.name
        )
        return mark_safe(owner_button)

    def get_storage_info(self, obj):
        storage_button = "<a class ='icon fa fa-detail' style='color: violet' href='/admin/AppleApp/appleinstancethroughstorage/?q={}'>{}</a>".format(
            obj.uid.hex,
            "detail"
        )
        return mark_safe(storage_button)

    def get_storage_change_info(self, obj):
        storage_change_button = "<a class ='icon fa fa-detail' style='color: violet' href='/admin/AppleApp/storagepoolquantitychangelog/?q={}'>{}</a>".format(
            obj.uid.hex,
            "detail"
        )
        return mark_safe(storage_change_button)

    def get_available(self, obj):
        return obj.is_available

    get_owner_type.short_description = "商户类型"
    get_user_phone.short_description = "商户联系电话"
    get_available.short_description = "是否愿意出售"
    get_owner_info.short_description = "商户名称"
    get_storage_info.short_description = "该批次苹果存储详情"
    get_storage_change_info.short_description = "该批次苹果出售流水"

    get_available.boolean = True

    get_owner_info.allow_tags = True
    get_storage_info.allow_tags = True

    list_filter = ["type", "level", "maturity", "pesticide_residue", "packing_type", "owner__owner_type", "price",
                   "product_time", "is_available", "is_empty"]

    owner_info = ["get_owner_type", "get_user_phone", "get_owner_info", "get_storage_info", "get_storage_change_info"]

    raw_info = ["batch_name", "type", "level", "maturity", "pesticide_residue", "packing_type", "price",
                "sum_remaining", "product_time", "get_available", "is_empty"]

    list_display = raw_info + owner_info
    list_display_links = ["type"]
    search_fields = ["owner__user__uid", "owner__user__name"]

    fieldsets = (
        (
            'instance_feature',
            {
                'fields':
                    [
                        "batch_name", "type", "level", "maturity", "pesticide_residue", "packing_type", "sum_remaining",
                        "price", "product_time", "is_available", "is_empty"
                    ]
            }
        ),
        (
            'owner',
            {
                'fields': ["owner"]
            }
        ),
    )


@admin.register(StoragePoolType)
class AdminStoragePoolType(AdminAbstract):
    pass


@admin.register(StoragePool)
class AdminStoragePool(AdminAbstract):
    def get_owner_type_name(self, obj):
        res = obj.owner
        if res is None:
            return "None"
        else:
            return res.user.name

    get_owner_type_name.short_description = "仓库法人"
    list_display = ["get_owner_type_name", "pool_type", "location", "phone_number", "capacity", "is_internal_managed"]
    list_filter = ["pool_type", "is_internal_managed"]


@admin.register(AppleInstanceThroughStorage)
class AdminAppleInstanceThroughStorage(AdminAbstract):

    def get_owner_type_name(self, obj):
        res = obj.storage_pool.owner
        if res is None:
            return "None"
        else:
            return res.user.name

    def get_pool_name(self, obj):
        return obj.storage_pool.location

    def get_pool_type(self, obj):
        return obj.storage_pool.pool_type

    def get_pool_manage_type(self, obj):
        return obj.storage_pool.is_internal_managed

    def get_record_info(self, obj):
        recode_info_button = "<a class ='icon fa fa-detail' style='color: violet' href='/admin/AppleApp/storagepoolquantitychangelog/?q={}'>{}</a>".format(
            obj.uid.hex,
            "detail"
        )
        return mark_safe(recode_info_button)

    get_owner_type_name.short_description = "仓库所有者"
    get_pool_name.short_description = "仓库地址"
    get_pool_type.short_long_description = "仓库类型"
    get_pool_manage_type.short_description = "该仓库是否为内部维护类型"
    get_record_info.short_description = "该批次苹果出售流水详情"

    get_pool_manage_type.boolean = True
    get_record_info.allow_tags = True
    list_display = ["get_owner_type_name", "get_pool_type", "get_pool_name", "get_pool_manage_type", "remaining",
                    "incoming_time", "get_record_info"]
    list_filter = ["storage_pool__pool_type", "storage_pool__is_internal_managed"]
    search_fields = ["apple_instance__uid"]


@admin.register(StoragePoolQuantityChangeLogType)
class AdminStoragePoolQuantityChangeLogType(AdminAbstract):
    pass


@admin.register(StoragePoolQuantityChangeLog)
class AdminStoragePoolQuantityChangeLog(AdminAbstract):
    list_display = ["record_type", "change_number", "remaining", "note"]
    list_filter = ["record_type", "remaining"]
    search_fields = ["storage__uid", "storage__apple_instance__uid"]
