from confapp import conf

from resources.models import Building

from .resources import ResourcesListWidget, ResourcesEditFormWidget


class BuildingsListWidget(ResourcesListWidget):
    """
    """

    UID = 'buildings'
    TITLE = 'Buildings'

    MODEL = Building

    EDITFORM_CLASS = ResourcesEditFormWidget

    LIST_DISPLAY = ['name']

    SEARCH_FIELDS = ['name__icontains']

    FIELDSETS = [
        'name',
        'description',
        'ImagesListWidget',
        'MaintenanceListWidget',
        'MaintenanceContractListWidget',
    ]

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'building'
    ORQUESTRA_MENU_ORDER = 1
    # =========================================================================
