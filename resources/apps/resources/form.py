from pyforms_web.widgets.django import ModelFormWidget
from pyforms.controls import ControlButton
from resources.models import Resource

from .images import ImagesListWidget
from .maintenance import MaintenanceListWidget
from .maintenance_contract.inline_list import MaintenanceContractInlineListWidget
from .accesses.list import ResourceAccessList


class InlineResourceAccessList(ResourceAccessList):
    pass


class ResourceFormWidget(ModelFormWidget):

    MODEL = Resource

    INLINES = [
        ImagesListWidget,
        MaintenanceListWidget,
        MaintenanceContractInlineListWidget,
        InlineResourceAccessList
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._contractsbtn = ControlButton('Maintenance contracts', label_visible=False)
        self._accessesbtn = ControlButton('Users accesses', label_visible=False)

        self.__require_access_changed_evt()

        #self.req_access.label_visible = False
        self.req_access.changed_event = self.__require_access_changed_evt

    def __require_access_changed_evt(self):

        if self.req_access.value:
            self.access_req.show()
        else:
            self.access_req.hide()


    @property
    def title(self):
        obj = self.model_object
        if obj is None:
            return ModelFormWidget.title.fget(self)
        else:
            return obj.name

    @title.setter
    def title(self, value):
        ModelFormWidget.title.fset(self, value)