from django.db import models
from django.conf import settings


class ResourceAccess(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resource = models.ForeignKey(to='resources.Resource', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Resource Access"
        verbose_name_plural = "Resource Accesses"
