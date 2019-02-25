from pyforms.basewidget import segment
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from resources.models import Maintenance
from resources.models import MaintenanceContract

STYLE_SEGMENT_BASIC = 'border: 0; box-shadow: 0 0; padding: 0'


class MaintenanceFormWidget(ModelFormWidget):

    TITLE = 'Intervention'

    FIELDSETS = [
        (
            segment(
                ('maintenance_type', 'date'),
                'company',
                'quote_file',
                style=STYLE_SEGMENT_BASIC,
            ),
            segment(('contract', 'cost'), 'notes', style=STYLE_SEGMENT_BASIC),
        )
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contract.changed_event = self.__on_contract_change

    def __on_contract_change(self):
        """Update Company and Cost fields to reflect the selected Contract."""
        if self.contract.value:
            contract_pk = self.contract.value
            contract = MaintenanceContract.objects.get(pk=contract_pk)
            self.company.value = contract.company.pk
            self.cost.value = 0
        else:
            self.company.value = None
            self.cost.value = None


class MaintenanceListWidget(ModelAdminWidget):
    TITLE = 'Interventions'

    MODEL = Maintenance
    EDITFORM_CLASS = MaintenanceFormWidget
    LIST_DISPLAY = ['date', 'maintenance_type', 'cost', 'company']
