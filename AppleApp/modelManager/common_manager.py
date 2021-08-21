from django.db import models
from django.db.models import QuerySet


class CommonQuerySet(QuerySet):
    def update(self, **kwargs):
        return super().update(**kwargs)

    def create(self, **kwargs):
        return super().create(**kwargs)


class CommonManager(models.Manager):

    def get_queryset(self):
        return CommonQuerySet(self.model, using=self._db)


