from confapp import conf

from resources.models import Room

from .resources import ResourcesListWidget, ResourcesEditFormWidget


class RoomsEditForm(ResourcesEditFormWidget):
    FIELDSETS = [('name', 'building_floor', 'biosafety_level'), 'description']


class RoomsListWidget(ResourcesListWidget):
    """
    """

    UID = 'rooms'
    TITLE = 'Rooms'

    MODEL = Room

    EDITFORM_CLASS = RoomsEditForm

    LIST_DISPLAY = ['name', 'building_floor', 'biosafety_level']

    LIST_FILTER = ['building_floor', 'biosafety_level']

    SEARCH_FIELDS = ['name__icontains']

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME_FULL
    ORQUESTRA_MENU = 'left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'building'
    ORQUESTRA_MENU_ORDER = 1
    # =========================================================================
