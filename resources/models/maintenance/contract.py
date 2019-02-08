from django.db import models


class MaintenanceContract(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    contract_file = models.FileField(
        upload_to='resources/maintenance/contracts', blank=True
    )

    company = models.ForeignKey(to='supplier.Supplier', on_delete=models.CASCADE)
    resources = models.ManyToManyField(
        to='resources.Resource', related_name='maintenance_contracts'
    )

    def __str__(self):
        return "Maintenance Contract #{}".format(self.pk)
