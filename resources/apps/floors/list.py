from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from resources.models import Floor
from .form import FloorsEditForm

class FloorsListWidget(ModelAdminWidget):

    UID = 'floors'
    TITLE = 'Floors'

    MODEL = Floor

    EDITFORM_CLASS = FloorsEditForm

    LIST_DISPLAY = ['name', 'level', 'at_building']
    SEARCH_FIELDS = ['name__icontains']

    USE_DETAILS_TO_EDIT = False

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'building'
    ORQUESTRA_MENU_ORDER = 1
    # =========================================================================
