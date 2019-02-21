from django.db import models
from model_utils.managers import InheritanceManager


class Resource(models.Model):
    """
    A Resource defined with a unique name.
    Should be used as a base model.
    Inheriting from this model gives the possibility to assign images,
    and manage maintenance and access records.
    """

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    req_access = models.BooleanField('Require access', default=False)
    access_req = models.TextField('Access requirements', blank=True, null=True)

    biosafety_risks = models.ManyToManyField('biosafety.Risk', blank=False)

    objects = InheritanceManager()

    def __str__(self):
        return self.name or f"{self._meta.verbose_name.title()} #{self.id}"

    @staticmethod
    def autocomplete_search_fields():
        return ['name__icontains']