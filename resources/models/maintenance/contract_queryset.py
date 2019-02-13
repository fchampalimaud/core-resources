from django.db import models
from django.utils import timezone


class ContractQuerySet(models.QuerySet):

    def active(self):
        now = timezone.now()
        return self.filter(start_date__lte=now, end_date__gte=now)
