from pyforms.basewidget import segment
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms.controls import ControlCheckBox
from resources.models import MaintenanceContract

from .form import MaintenanceContractFormWidget

from .list import MaintenanceContractListWidget



class MaintenanceContractInlineListWidget(MaintenanceContractListWidget):

    UID = None

    USE_DETAILS_TO_ADD  = False
    USE_DETAILS_TO_EDIT = False

    def __init__(self, *args, **kwargs):

        self._active_filter = ControlCheckBox(
            'Only active',
            default=True,
            label_visible=False,
            changed_event=self.populate_list
        )

        super().__init__(*args, **kwargs)


    def has_add_permissions(self):
        return False

    def get_queryset(self, request, qs):

        qs = qs.filter(resources__id=self.parent_pk)

        if self._active_filter.value:
            qs = qs.active()

        return qs


    def get_toolbar_buttons(self, has_add_permission=False):
        return (
            '_active_filter',' '
        )

