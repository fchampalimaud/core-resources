from django.db import models
from .resource import Resource


class Area(Resource):
    """A collection of one or more Rooms."""

    sector = models.ForeignKey(
        'self', blank=True, null=True, related_name='subareas', on_delete=models.CASCADE
    )

    rooms = models.ManyToManyField(
        'resources.Room',
        verbose_name='rooms',
        blank=True,
        help_text=(
            'The rooms assigned to this area. A user with access to this '
            'area will have access to its rooms.'
        ),
        related_name="areas",
    )
