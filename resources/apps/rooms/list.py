from confapp import conf

from resources.models import Room

from resources.apps.resources.list import ResourcesListWidget
from .form import RoomsEditForm
from .create import RoomCreateForm

class RoomsListWidget(ResourcesListWidget):
    """
    """

    UID = 'rooms'
    TITLE = 'Rooms'

    MODEL = Room


    ADDFORM_CLASS = RoomCreateForm
    EDITFORM_CLASS = RoomsEditForm

    LIST_DISPLAY = ['name', 'building_floor', 'biosafety_level']

    LIST_FILTER = ['building_floor', 'biosafety_level']

    SEARCH_FIELDS = ['name__icontains']



    USE_DETAILS_TO_EDIT = False



    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME_FULL
    ORQUESTRA_MENU = 'middle-left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'cube'
    ORQUESTRA_MENU_ORDER = 1
    # =========================================================================
