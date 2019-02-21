from pyforms.basewidget import segment
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms.controls import ControlCheckBox
from resources.models import MaintenanceContract

from .form import MaintenanceContractFormWidget

from confapp import conf

class MaintenanceContractListWidget(ModelAdminWidget):

    UID   = 'maintenance-contracts'
    TITLE = 'Maintenance contracts'
    MODEL = MaintenanceContract

    EDITFORM_CLASS = MaintenanceContractFormWidget

    LIST_DISPLAY = ['id', 'start_date', 'end_date', 'company']


    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>ResourcesDashboardApp'
    ORQUESTRA_MENU_ICON = 'wrench'
    ORQUESTRA_MENU_ORDER = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # customize first column header
        self._list.headers = ['#', 'Start date', 'End date', 'Company']
