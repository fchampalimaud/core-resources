from django.db import models
from .resource import Resource
class Room(Resource):

    building_floor = models.ForeignKey(
        to='resources.Floor', verbose_name='Floor', on_delete=models.CASCADE
    )

    biosafety_level = models.ForeignKey('biosafety.Level', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-building_floor__level', 'name')

    def __str__(self):
        return f"{self.name} ({self.building_floor})"
