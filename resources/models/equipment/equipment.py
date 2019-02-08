from django.db import models
from resources.models.resource import Resource
from resources.models.equipment.querysets.equipment import EquipmentQuerySet


class Equipment(Resource):

    brand = models.CharField(max_length=80)
    product_number = models.CharField(
        verbose_name='Model / Product Number', max_length=80
    )
    url = models.URLField(verbose_name='URL', blank=True)
    notes = models.TextField(blank=True)

    uses_external_booking = models.BooleanField(
        default=False, help_text='e.g. iLab, Agendo'
    )
    is_missing = models.BooleanField(
        verbose_name='Out for repair / outreach events',
        default=False,
        help_text='Use the notes field to provide more information.',
    )

    # TODO make fields mandatory after introducing existing equipment in the DB
    acquisition_date = models.DateField(blank=True, null=True)
    warranty = models.PositiveSmallIntegerField(
        blank=True, null=True, help_text='years'
    )

    disposal_date = models.DateField(blank=True, null=True)

    an = models.CharField(verbose_name='Asset Number', max_length=50, blank=True)
    sn = models.CharField(verbose_name='Serial Number', max_length=50)

    sop = models.FileField(
        upload_to='equipment/sop',
        verbose_name='Standard Operating Procedure',
        blank=True,
    )

    category = models.ForeignKey(
        to='resources.EquipmentCategory', on_delete=models.CASCADE
    )
    company = models.ForeignKey(to='supplier.Supplier', on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        to='research.Group',
        help_text='Leave blank for common use equipment.',
        related_name='equipments',
        blank=True,
    )
    location = models.ForeignKey(to='resources.Room', on_delete=models.CASCADE)
    responsible = models.ForeignKey(
        to='humanresources.Person',
        blank=True,
        null=True,
        help_text='The person you should contact first',
        on_delete=models.CASCADE,
    )

    objects = EquipmentQuerySet.as_manager()

    class Meta:
        verbose_name = "Equipment"

    def is_available(self):
        return not (self.is_missing or self.disposal_date)

    is_available.short_description = 'available'
    is_available.boolean = True
