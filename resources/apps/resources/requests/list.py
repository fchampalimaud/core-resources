from pyforms_web.widgets.django import ModelAdminWidget
from resources.models import AccessRequest
from .form import AccessRequestFormWidget
from confapp import conf

class AccessRequestList(ModelAdminWidget):

    UID = 'accesses-requests'
    TITLE = 'Requests'


    EDITFORM_CLASS = AccessRequestFormWidget

    USE_DETAILS_TO_EDIT = False

    MODEL = AccessRequest
    LIST_DISPLAY = ['requested_by','resource', 'requested_on']

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>ResourcesDashboardApp'
    ORQUESTRA_MENU_ICON = 'key yellow'
    ORQUESTRA_MENU_ORDER = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def has_add_permissions(self):
        return False



