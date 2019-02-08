from pyforms_web.widgets.django import ModelAdminWidget
from resources.models import ResourceAccess
from confapp import conf

class ResourceAccessList(ModelAdminWidget):

    UID = 'access-list'
    TITLE = 'Access list'

    MODEL = ResourceAccess
    LIST_DISPLAY = ['user']

    LIST_DISPLAY = ['resource', 'user', 'start_date', 'end_date']

    SEARCH_FIELDS = ['user__username', 'resource__name']

    FIELDSETS = [
        ('user', 'resource'),
        ('start_date', 'end_date')
    ]


    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'lock'
    ORQUESTRA_MENU_ORDER = 50



