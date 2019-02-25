from pyforms.basewidget import no_columns

from resources.apps.resources.form import ResourceFormWidget
from pyforms.controls import ControlButton
from resources.models import Building
from confapp import conf

class BuildingForm(ResourceFormWidget):

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    MODEL = Building

    INLINES = ResourceFormWidget.INLINES

    FIELDSETS = [
        {
            'a:Building': [
                ('name', 'req_access'),
                'description',
                ('managers', 'biosafety_risks'),
                'access_req',
                no_columns('_contractsbtn', '_accessesbtn'),
            ],
            'b:Images': ['ImagesListWidget'],
            'b:Interventions': ['MaintenanceListWidget']
        }
    ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name.field_css = 'fourteen wide'
        self.req_access.field_css = 'three wide'

        