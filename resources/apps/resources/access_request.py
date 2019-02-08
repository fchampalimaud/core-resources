from pyforms_web.widgets.django import ModelAdminWidget
from resources.models import AccessRequest
from confapp import conf

class AccessRequestList(ModelAdminWidget):

    UID = 'accesses-requests'
    TITLE = 'Requests'

    MODEL = AccessRequest
    LIST_DISPLAY = ['user']

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'cubes'
    ORQUESTRA_MENU_ORDER = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



