from pyforms_web.widgets.django import ModelAdminWidget
from resources.models import ResourceAccess
from .form import ResourceAccessFormWidget, ResourceAccessCreateForm
from confapp import conf

class ResourceAccessList(ModelAdminWidget):

    UID = 'access-list'
    TITLE = 'Access list'

    MODEL = ResourceAccess

    ADDFORM_CLASS  = ResourceAccessCreateForm
    EDITFORM_CLASS = ResourceAccessFormWidget

    LIST_DISPLAY = ['resource', 'user', 'start_date', 'end_date', 'is_revoked']

    LIST_FILTER = ['resource', 'user', 'start_date', 'end_date']

    SEARCH_FIELDS = ['user__username', 'resource__name']

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>ResourcesDashboardApp'
    ORQUESTRA_MENU_ICON = 'lock yellow'
    ORQUESTRA_MENU_ORDER = 50