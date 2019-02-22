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

    reason = models.TextField(
        'Access details',
        blank=True,
        help_text='Why and how you want to access the resource. Describe also if you fulfill the access requirements.'
    )

    comment = models.TextField(
        'Comment',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Requested by [{self.requested_by}] to [{self.resource}]: {self.is_approved()}"


    def is_closed(self):
        return self.closed_on is not None and self.closed_by is not None
    is_closed.short_description = 'Closed'

    def is_approved(self):
        if self.is_closed() and self.access is not None:
            return True
        elif self.is_closed() and self.access is None:
            return False
        else:
            return None
    is_approved.short_description = 'Approved'


    def accept(self, approved_by, until=None, comment=None):
        now = timezone.now()

        self.closed_by = approved_by
        self.closed_on = now
        self.comment   = comment

        self.access = ResourceAccess(
            user        = self.requested_by,
            resource    = self.resource,
            start_date  = now,
            end_date    = until,
            created_by  = approved_by
        )
        self.access.save()
        self.save()

    def reject(self, rejected_by, comment=None):
        now = timezone.now()

        self.closed_by = rejected_by
        self.closed_on = now
        self.access    = None
        self.comment   = comment
        self.save()




