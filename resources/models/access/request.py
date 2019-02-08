from django.db import models
from model_utils.models import StatusModel
from model_utils import Choices


class AccessRequest(StatusModel):
    STATUS = Choices(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    requested_on = models.DateTimeField(auto_now_add=True, blank=True)
