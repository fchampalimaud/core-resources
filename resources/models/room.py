from django.db import models
from .resource import Resource
from model_utils import Choices


class Room(Resource):

    BIOSAFETY_LEVELS = Choices(
        (0, 'na', 'N/A'),
        (1, 'bsl1', 'BSL-1'),
        (2, 'bsl2', 'BSL-2'),
        (3, 'bsl3', 'BSL-3'),
        (4, 'bsl4', 'BSL-4'),
    )

    biosafety_level = models.IntegerField(
        choices=BIOSAFETY_LEVELS, default=BIOSAFETY_LEVELS.na
    )

    building_floor = models.ForeignKey(
        to='resources.Floor', verbose_name='Floor', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-building_floor__level', 'name')

    def __str__(self):
        return f"{self.name} ({self.building_floor})"
