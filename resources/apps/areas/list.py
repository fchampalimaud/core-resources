from confapp import conf

from resources.models import Area

from resources.apps.resources.list import ResourcesListWidget

from .form import AreasEditForm

class AreasListWidget(ResourcesListWidget):

    UID = 'areas'
    TITLE = 'Areas'

    MODEL = Area

    EDITFORM_CLASS = AreasEditForm

    LIST_DISPLAY = ['name']

    LIST_FILTER = ['rooms']

    SEARCH_FIELDS = ['name__icontains']

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME_FULL
    ORQUESTRA_MENU = 'middle-left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'map'
    ORQUESTRA_MENU_ORDER = 2
    # =========================================================================
