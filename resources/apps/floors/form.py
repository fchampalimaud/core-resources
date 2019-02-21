from pyforms_web.organizers import segment
from resources.apps.rooms.list import RoomsListWidget
from resources.apps.resources.form import ResourceFormWidget
from confapp import conf

class FloorsEditForm(ResourceFormWidget):

    LAYOUT_POSITION         = conf.ORQUESTRA_NEW_TAB

    HAS_CANCEL_BTN_ON_EDIT  = False
    CLOSE_ON_REMOVE         = True

    INLINES = [
        RoomsListWidget
    ]

    FIELDSETS = [
        {
            'a:Floor':[
                ('name', 'level', 'at_building','req_access'),
                'access_req',
                'description',
                'biosafety_risks',
                'req_access',
                'access_req',
                segment(
                    'RoomsListWidget',
                    css='red'
                ),
                'managers'
            ],
            'b:Access list': ['InlineResourceAccessList'],
                             'c:Maintenance contracts': ['MaintenanceContractInlineListWidget'],
            'e:Maintenance': ['MaintenanceListWidget'],
            'a:Images': ['ImagesListWidget'],
        }
    ]