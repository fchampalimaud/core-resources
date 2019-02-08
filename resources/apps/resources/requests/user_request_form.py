from pyforms_web.widgets.django import ModelFormWidget
from resources.models import AccessRequest
from confapp import conf

class UserRequestForm(ModelFormWidget):

    UID = 'request-access'
    TITLE = 'Access request form'

    MODEL = AccessRequest

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME_FULL
    ORQUESTRA_MENU = 'middle-left>DashboardApp'
    ORQUESTRA_MENU_ICON = 'key'
    ORQUESTRA_MENU_ORDER = -1
    # =========================================================================
