from pyforms_web.widgets.django import ModelFormWidget
from resources.models import Resource

from .images import ImagesListWidget
from .maintenance import MaintenanceListWidget
from .maintenance_contract.inline_list import MaintenanceContractInlineListWidget
from .access import ResourceAccessList


class InlineResourceAccessList(ResourceAccessList):
    pass


class ResourceFormWidget(ModelFormWidget):

    MODEL = Resource

    #FIELDSETS = ['name', 'description']

    INLINES = [
        ImagesListWidget,
        MaintenanceListWidget,
        MaintenanceContractInlineListWidget,
        InlineResourceAccessList
    ]

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