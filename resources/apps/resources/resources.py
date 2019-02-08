from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from resources.models.resource import Resource

from .images import ImagesListWidget
from .maintenance import MaintenanceListWidget
from .maintenance_contract import MaintenanceContractListWidget


class ResourcesEditFormWidget(ModelFormWidget):
    MODEL = Resource
    FIELDSETS = ['name', 'description']


class ResourcesListWidget(ModelAdminWidget):
    """
    Base class used by all Resource type apps.
    """

    UID = 'resources'
    TITLE = 'Resources'

    MODEL = Resource

    EDITFORM_CLASS = ResourcesEditFormWidget

    LIST_DISPLAY = ['name']
    SEARCH_FIELDS = ['name__icontains']
    INLINES = [ImagesListWidget, MaintenanceListWidget, MaintenanceContractListWidget]
