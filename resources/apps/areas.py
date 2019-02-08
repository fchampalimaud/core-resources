from confapp import conf

from resources.models import Area

from .resources import ResourcesListWidget, ResourcesEditFormWidget


class AreasEditForm(ResourcesEditFormWidget):
    FIELDSETS = ['name', 'rooms', 'description']


class AreasListWidget(ResourcesListWidget):
    """
    """

    UID = 'areas'
    TITLE = 'Areas'

    MODEL = Area

    EDITFORM_CLASS = AreasEditForm

    LIST_DISPLAY = ['name', 'ImagesListWidget']

    LIST_FILTER = ['rooms']

    SEARCH_FIELDS = ['name__icontains']

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME_FULL
    ORQUESTRA_MENU = 'left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'map'
    ORQUESTRA_MENU_ORDER = 1
    # =========================================================================
