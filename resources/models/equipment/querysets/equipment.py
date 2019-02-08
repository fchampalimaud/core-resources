from django.db import models
from django.utils.timezone import datetime


class EquipmentQuerySet(models.QuerySet):
    def uncovered(self):
        """No valid maintenance contracts."""
        today = datetime.today()

        no_contract = models.Q(equipmentmaintenancecontract__isnull=True)
        invalid_contract = (
            models.Q(equipmentmaintenancecontract__start_date__gt=today)
            | models.Q(equipmentmaintenancecontract__end_date__lt=today)
        )

        return self.filter(no_contract | invalid_contract)

    def missing_details(self):
        no_asset_number = models.Q(an='')
        no_acquisition_date = models.Q(acquisition_date__isnull=True)
        no_warranty = models.Q(warranty__isnull=True)
        return self.filter(no_asset_number | no_acquisition_date | no_warranty)

    def unavailable(self):
        missing = models.Q(is_missing=True)
        disposed = models.Q(disposal_date__isnull=False)
        return self.filter(missing | disposed)
