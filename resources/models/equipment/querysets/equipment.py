from django.db import models
from django.utils.timezone import datetime


class EquipmentQuerySet(models.QuerySet):


    def missing_details(self):
        no_asset_number = models.Q(an='')
        no_acquisition_date = models.Q(acquisition_date__isnull=True)
        no_warranty = models.Q(warranty__isnull=True)
        return self.filter(no_asset_number | no_acquisition_date | no_warranty)

    def unavailable(self):
        missing = models.Q(is_missing=True)
        disposed = models.Q(disposal_date__isnull=False)
        return self.filter(missing | disposed)
