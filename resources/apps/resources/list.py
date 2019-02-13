from pyforms_web.widgets.django import ModelAdminWidget
from resources.models.resource import Resource

from .images import ImagesListWidget
from .maintenance import MaintenanceListWidget
from .maintenance_contract.inline_list import MaintenanceContractInlineListWidget

from .form import ResourceFormWidget

class ResourcesListWidget(ModelAdminWidget):
    """
    Base class used by all Resource type apps.
    """

    UID = 'resources'
    TITLE = 'Resources'

    MODEL = Resource

    #EDITFORM_CLASS = ResourceFormWidget

    LIST_DISPLAY = ['name']
    SEARCH_FIELDS = ['name__icontains']
    INLINES = [ImagesListWidget, MaintenanceListWidget, MaintenanceContractInlineListWidget]
