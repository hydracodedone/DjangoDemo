# encoding:UTF-8

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models import FloatField, Sum
from django.utils.safestring import mark_safe

from AppleApp.models import LoginUser, OwnerType, Owner, AppleType, AppleLevel, AppleMaturity, ApplePesticideResidue, \
    ApplePackingType, AppleInstance


class AdminAbstract(ModelAdmin):
    actions_selection_counter = True
    date_hierarchy = "create_time"
    empty_value_display = "-empty-"
    list_max_show_all = 100
    preserve_filters = False
    list_select_related = True
    show_full_result_count = False


@admin.register(LoginUser)
class AdminLoginUser(AdminAbstract):
    list_display = ["name", "phone_number", "login_name", "login_password"]
    list_editable = ["name", "phone_number", "login_name"]
    search_fields = ["name", "phone_number"]
    list_display_links = None


@admin.register(OwnerType)
class AdminOwnerType(AdminAbstract):
    pass


@admin.register(Owner)
class AdminOwner(AdminAbstract):
    list_filter = ["owner_type"]
    search_fields = ["user__uid", "user__name", "user__phone_number"]
    list_select_related = ["user"]

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

    def record_button(self, obj):
        button = "<a class ='icon fa fa-detail' style='color: violet' " \
                 "href='/admin/AppleApp/appleinstance/?q={}'>detail</a>".format(obj.user.uid)

        return mark_safe(button)

    def get_name(self, obj):
        return obj.user.name

    get_name.short_description = "name"
    record_button.short_description = "detail"
    get_apple_avaliable_remaining.short_description = "avaliable_remaining"
    get_apple_sum_remaining.short_description = "sum_remaining"

    record_button.allow_tags = True

    list_display = ["get_name", "get_apple_sum_remaining", "get_apple_avaliable_remaining", "record_button"]


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
        return obj.owner.owner_type.owner_name

    def get_user_phone(self, obj):
        return obj.owner.user.phone_number

    def get_user_name(self, obj):
        button = "<a class ='icon fa fa-detail' style='color: violet' " \
                 "href='/admin/AppleApp/owner/?q={}'>{}</a>".format(obj.owner.user.uid, obj.owner.user.name)
        return mark_safe(button)

    def get_available(self, obj):
        return obj.is_available

    get_owner_type.short_description = "owner_type"
    get_user_phone.short_description = "owner_phone"
    get_available.short_description = "is_available"
    get_user_name.short_description = "owner"

    get_available.boolean = True
    get_user_name.allow_tags = True

    list_filter = ["type", "level", "maturity", "pesticide_residue", "packing_type", "owner__owner_type", "price",
                   "product_time", "is_available"]

    owner_info = ["get_owner_type", "get_user_name", "get_user_phone"]

    raw_info = ["type", "level", "maturity", "pesticide_residue", "packing_type", "price", "sum_remaining",
                "product_time", "get_available"]

    list_display = raw_info + owner_info

    search_fields = ["owner__uid", "owner__user__name"]
