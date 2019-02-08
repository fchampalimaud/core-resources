from django.core.validators import RegexValidator
from django.db import models


class EquipmentSection(models.Model):

    equipment = models.ForeignKey(to='resources.Equipment', on_delete=models.CASCADE)
    owners = models.ManyToManyField(to='research.Group')
    row = models.CharField(
        verbose_name='row',
        max_length=1,
        validators=[RegexValidator(regex=r'^[0-9]$', message='Must be a number')],
        help_text='1-9',
    )
    col = models.CharField(
        verbose_name='column',
        max_length=1,
        validators=[
            RegexValidator(regex=r'^[A-Z]$', message='Must be a capital letter')
        ],
        help_text='A-Z',
    )

    class Meta:
        verbose_name = "Equipment section"
        ordering = ('equipment', 'col', 'row')
        unique_together = ('equipment', 'row', 'col')

    def __str__(self):
        return f"Rack {self.label} on {self.equipment}"

    @property
    def label(self):
        return self.col + self.row
