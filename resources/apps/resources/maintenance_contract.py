from pyforms.basewidget import segment
from pyforms_web.widgets.django import ModelAdminWidget

from resources.models import MaintenanceContract

STYLE_SEGMENT_BASIC = 'border: 0; box-shadow: 0 0; padding: 0'


class MaintenanceContractListWidget(ModelAdminWidget):
    MODEL = MaintenanceContract
    LIST_DISPLAY = ['id', 'start_date', 'end_date', 'company']
    FIELDSETS = [
        (
            segment(
                ('start_date', 'end_date'), 'contract_file', style=STYLE_SEGMENT_BASIC
            ),
            segment('company', 'notes', style=STYLE_SEGMENT_BASIC),
        )
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # customize first column header
        self._list.headers = ['#', 'Start date', 'End date', 'Company']
