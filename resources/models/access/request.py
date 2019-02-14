from django.db import models
from django.utils import timezone
from .access import ResourceAccess

class AccessRequest(models.Model):

    requested_on = models.DateTimeField(auto_now_add=True, blank=True)
    requested_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='access_requester', default=None)

    closed_on = models.DateTimeField('Closed on', blank=True, null=True)
    closed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='access_closer', default=None, blank=True, null=True)
    access    = models.ForeignKey('ResourceAccess', on_delete=models.CASCADE, null=True, blank=True)

    resource  = models.ForeignKey('Resource', on_delete=models.CASCADE, limit_choices_to={'req_access': True})

    reason = models.TextField('Reason', blank=True)


    def accept(self, user):
        now = timezone.now()

        self.closed_by = user
        self.closed_on = now

        self.access = ResourceAccess(user=user, resource=self.resource, start_date=now)
        self.access.save()

        self.save()

    def reject(self, user):
        now = timezone.now()

        self.closed_by = user
        self.closed_on = now
        self.access = None
        self.save()




