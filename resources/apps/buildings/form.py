from pyforms.basewidget import segment

from ..floors.list import FloorsListWidget
from resources.apps.resources.form import ResourceFormWidget
from resources.models import Building


class BuildingForm(ResourceFormWidget):

    MODEL = Building

    INLINES = ResourceFormWidget.INLINES + [FloorsListWidget]

    FIELDSETS = [
        {
            'a:Building':[
                'name',
                'description',
                'biosafety_risks',
                segment(
                    'FloorsListWidget',
                    css='secondary'
                )
            ],
            'c:Maintenance': 'MaintenanceListWidget',
            'b:Maintenance contracts': 'MaintenanceContractListWidget',
            'a:Images': 'ImagesListWidget'
        }
    ]
