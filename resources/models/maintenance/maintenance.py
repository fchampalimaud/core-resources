from django.db import models
from model_utils import Choices


class Maintenance(models.Model):

    MAINTENANCE_TYPES = Choices(
        (0, 'corrective', 'Corrective'),
        (1, 'predictive', 'Predictive'),
        (2, 'preventive', 'Preventive'),
    )

    maintenance_type = models.IntegerField(
        choices=MAINTENANCE_TYPES, default=MAINTENANCE_TYPES.preventive
    )

    date = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(blank=True)

    quote_file = models.FileField(upload_to='resources/maintenance/quotes', blank=True)

    company = models.ForeignKey(to='supplier.Supplier', on_delete=models.CASCADE)
    contract = models.ForeignKey(
        to='resources.MaintenanceContract',
        help_text='Select a Maintenance Contract covering this service.',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    resource = models.ForeignKey(to='resources.Resource', on_delete=models.CASCADE)


