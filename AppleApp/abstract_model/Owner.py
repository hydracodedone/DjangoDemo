from django.db.models import QuerySet

from AppleApp.abstract_model.common import CommonManager, CommonAbstractModel


class OwnerQuerySet(QuerySet):
    def update(self, **kwargs):
        return super().update(**kwargs)

    def create(self, **kwargs):
        return super().create(**kwargs)

    def delete(self):
        self.update(is_deleted=True)


class OwnerManagert(CommonManager):
    def get_queryset(self):
        return OwnerQuerySet(self.model, using=self._db)


class OwnerAbstractModel(CommonAbstractModel):
    class Meta:
        abstract = True

    def clean_fields(self, exclude=None):
        self.is_validate = False
        super().clean_fields()

    def clean(self):
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class OwnerObject(object):
    custom_objects = CommonManager()
