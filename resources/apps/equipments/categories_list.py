from pyforms_web.widgets.django import ModelAdminWidget
from resources.models import EquipmentCategory
from confapp import conf

class CategoriesList(ModelAdminWidget):

    UID = 'categories-list'
    TITLE = 'Categories'

    MODEL = EquipmentCategory

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>ResourcesDashboardApp'
    ORQUESTRA_MENU_ICON = 'cubes'
    ORQUESTRA_MENU_ORDER = 5
    # =========================================================================
