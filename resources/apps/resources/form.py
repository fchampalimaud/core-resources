from pyforms_web.widgets.django import ModelFormWidget
from resources.models import Resource

from .images import ImagesListWidget
from .maintenance import MaintenanceListWidget
from .maintenance_contract import MaintenanceContractListWidget

class ResourceFormWidget(ModelFormWidget):
    MODEL = Resource

    INLINES = [ImagesListWidget, MaintenanceListWidget, MaintenanceContractListWidget]
    FIELDSETS = ['name', 'description']
