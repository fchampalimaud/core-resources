from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta

class ResourceAccess(models.Model):
    start_date = models.DateField('Start')
    end_date   = models.DateField('End', null=True, blank=True)

    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resource = models.ForeignKey('resources.Resource', on_delete=models.CASCADE, limit_choices_to={'req_access': True})

    created_on = models.DateTimeField('Created on', auto_now=True)
    created_by = models.ForeignKey(
        'auth.User',
        on_delete    = models.CASCADE,
        related_name = 'resourceaccess_creator'
    )

    revoked_by = models.ForeignKey(
        'auth.User',
        on_delete    = models.CASCADE,
        related_name = 'resourceaccess_revoker',
        null         = True,
        blank        = True
    )

    class Meta:
        verbose_name        = "Resource access"
        verbose_name_plural = "Resource accesses"


    def is_revoked(self):
        return self.revoked_by is not None
    is_revoked.short_description = 'Revoked'


    def revoke(self, revoked_by):
        self.revoked_by = revoked_by
        self.end_date   = timezone.now() - timedelta(days=1)
        self.save()