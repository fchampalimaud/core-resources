from pyforms_web.widgets.django import ModelFormWidget
from resources.models import MaintenanceContract
from confapp import conf
from pyforms.basewidget import segment

class MaintenanceContractFormWidget(ModelFormWidget):

    MODEL = MaintenanceContract

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    FIELDSETS = [
        (
            segment(
                ('start_date', 'end_date'),
                'contract_file'
            ),
            segment('company', 'notes'),
        ),
        'resources'
    ]

    @property
    def title(self):
        obj = self.model_object
        if obj is None:
            return ModelFormWidget.title.fget(self)
        else:
            return str(obj)

    @title.setter
    def title(self, value):
        ModelFormWidget.title.fset(self, value)