from django.db import models
from .resource import Resource
from django.contrib.humanize.templatetags.humanize import ordinal


class Floor(Resource):
    level = models.SmallIntegerField(unique=True)

    at_building = models.ForeignKey(
        to='Building', verbose_name='Building', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-level',)

    def __str__(self):
        return f'{self.name} [{self.at_building}]'

        """
        if self.level < 0:
            return f"{ordinal(-self.level)} Basement"
        elif self.level == 0:
            return "Ground Floor"
        else:
            return f"{ordinal(self.level)} Floor"
        """

    def save(self):
        self.name = str(self)
        super().save()
