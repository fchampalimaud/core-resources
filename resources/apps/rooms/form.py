from confapp import conf
from pyforms_web.organizers import segment
from resources.apps.resources.form import ResourceFormWidget

from resources.apps.equipments.list import EquipmentListWidget

class RoomsEditForm(ResourceFormWidget):

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    HAS_CANCEL_BTN_ON_EDIT = False
    CLOSE_ON_REMOVE = True

    INLINES = ResourceFormWidget.INLINES + [EquipmentListWidget]

    FIELDSETS = [
        {
            'a:Building': [
                ('name', 'building_floor', 'biosafety_level'),
                'req_access',
                'description',
                'biosafety_risks',
                segment(
                    'EquipmentListWidget',
                    css='secondary'
                )
            ],
            'b:Access list': ['InlineResourceAccessList'],
            'c:Maintenance contracts': ['MaintenanceContractInlineListWidget'],
            'e:Maintenance': ['MaintenanceListWidget'],
            'a:Images': ['ImagesListWidget'],
        }
    ]
