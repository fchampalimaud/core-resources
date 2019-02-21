from django.conf import settings

from confapp import conf
from pyforms.basewidget import BaseWidget
from pyforms.basewidget import segment
from pyforms.controls import ControlButton
from pyforms.controls import ControlText
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from resources.models import Equipment
from resources.models import EquipmentCategory
from resources.models import EquipmentSection

from ..resources.list import ResourcesListWidget
from ..resources.form import ResourceFormWidget


STYLE_SEGMENT_BASIC = 'border: 0; box-shadow: 0 0; padding: 0'


class EquipmentRackListWidget(ModelAdminWidget):

    TITLE = 'Racks'

    MODEL = EquipmentSection
    LIST_DISPLAY = ['label', 'owners']
    FIELDSETS = [('col', 'row', 'owners')]


class EquipmentCategoryAddForm(BaseWidget):

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._name = ControlText('Name')
        self._save_btn = ControlButton(
            'Save', default=self.__save_btn_evt, label_visible=False
        )

        self.formset = ['_name', '_save_btn']

    def __save_btn_evt(self):
        value = self._name.value
        if value:
            obj = EquipmentCategory()
            obj.name = value.strip()
            obj.save()
            self.close()


class EquipmentEditForm(ResourceFormWidget):
    FIELDSETS = [
        ('name', 'location', 'category', '_new_category_btn'),
        {
            '1:Details': [
                (
                    segment(
                        'company',
                        ('brand', 'product_number'),
                        ('sn', 'an'),
                        'sop',
                        style=STYLE_SEGMENT_BASIC,
                    ),
                    'req_access',
                    'access_req',
                    segment('url', 'description', style=STYLE_SEGMENT_BASIC),
                )
            ],
            '2:Status': [
                (
                    segment(
                        ('acquisition_date', 'warranty'),
                        ('disposal_date', ' '),
                        'uses_external_booking',
                        'is_missing',
                        style=STYLE_SEGMENT_BASIC,
                    ),
                    segment('responsible', 'groups', style=STYLE_SEGMENT_BASIC),
                )
            ],
            '3:Images': ['ImagesListWidget'],
            '4:Racks': ['EquipmentRackListWidget'],
            'Maintenance': [
                'h3:Interventions',
                'MaintenanceListWidget',
                'MaintenanceContractInlineListWidget'
            ],
            'Notes': ['notes'],
        },
    ]

    INLINES = ResourceFormWidget.INLINES + [ EquipmentRackListWidget ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # FIXME how to add extra inline ???

        self._new_category_btn = ControlButton(
            label='<i class="plus icon"></i>',
            helptext='Add new category',
            default=self.__new_category_btn_evt,
            css='blue circular ui icon button',
        )

        self.notes.label = ''

    def __new_category_btn_evt(self):
        # FIXME the new value does not show up in the ComboBox
        EquipmentCategoryAddForm(title='Create a new equipment category')


class EquipmentListWidget(ResourcesListWidget):
    """
    """

    UID = 'equipment'
    TITLE = 'Equipment'

    MODEL = Equipment

    EDITFORM_CLASS = EquipmentEditForm

    LIST_DISPLAY = ['name', 'category', 'location', 'is_available']

    LIST_FILTER = ['category', 'location', 'acquisition_date', 'is_missing']

    SEARCH_FIELDS = ['name__icontains']

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left>ResourcesDashboardApp'
    ORQUESTRA_MENU_ICON = 'microchip'
    ORQUESTRA_MENU_ORDER = 3
    # =========================================================================
