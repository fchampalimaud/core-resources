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

    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, limit_choices_to={'req_access': True})