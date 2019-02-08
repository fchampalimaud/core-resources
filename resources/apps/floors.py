from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from resources.models import Floor


class FloorsEditForm(ModelFormWidget):
    FIELDSETS = [('name', 'level', 'at_building'), 'description']


class FloorsListWidget(ModelAdminWidget):
    """
    """

    UID = 'floors'
    TITLE = 'Floors'

    MODEL = Floor

    EDITFORM_CLASS = FloorsEditForm

    LIST_DISPLAY = ['name', 'level', 'at_building']

    LIST_FILTER = ['level', 'at_building']

    SEARCH_FIELDS = ['name__icontains']

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME_FULL
    ORQUESTRA_MENU = 'left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'building'
    ORQUESTRA_MENU_ORDER = 1
    # =========================================================================
