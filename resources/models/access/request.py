from django.db import models
from django.utils import timezone
from model_utils.models import StatusModel
from model_utils import Choices


class AccessRequest(StatusModel):
    STATUS = Choices(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    requested_on = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        abstract = True
