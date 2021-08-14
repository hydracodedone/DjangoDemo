from django.db import models
from django.db.models import QuerySet

from AppleApp.util.util import uuid_general, get_now_time


class CommonQuerySet(QuerySet):
    def update(self, **kwargs):
        return super().update(**kwargs)

    def create(self, **kwargs):
        return super().create(**kwargs)

    def delete(self):
        self.update(is_deleted=True)


class CommonManager(models.Manager):

    def get_queryset(self):
        return CommonQuerySet(self.model, using=self._db)


class CommonAbstractModel(models.Model):
    uid = models.UUIDField(primary_key=True, auto_created=True, db_index=True, default=uuid_general)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后一次更新时间")
    delete_time = models.DateTimeField(null=True, blank=True, verbose_name="删除时间")
    is_deleted = models.BooleanField(null=False, default=False, verbose_name="是否删除")

    class Meta:
        abstract = True

    def clean_fields(self, exclude=None):
        self.is_validate = False
        super().clean_fields()

    def clean(self):
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.delete_time = get_now_time()
        self.save()


class CommonObject(object):
    custom_objects = CommonManager()
