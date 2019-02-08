from django.db import models


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name = "Equipment Category"
        verbose_name_plural = "Equipment Categories"

    def __str__(self):
        return self.name
