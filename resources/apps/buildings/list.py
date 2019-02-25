from confapp import conf

from resources.models import Building

from resources.apps.resources.list import ResourcesListWidget
from .form import BuildingForm


class BuildingsListWidget(ResourcesListWidget):
    """
    """

    UID = 'buildings'
    TITLE = 'Buildings'

    MODEL = Building

    EDITFORM_CLASS = BuildingForm
    USE_DETAILS_TO_EDIT = False

    LIST_DISPLAY = ['name']

    SEARCH_FIELDS = ['name__icontains']

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>ResourcesDashboardApp'
    ORQUESTRA_MENU_ICON = 'building'
    ORQUESTRA_MENU_ORDER = 0
    # =========================================================================
