from pyforms.basewidget import no_columns, segment
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.widgets.django import ModelViewFormWidget
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms.controls import ControlButton
from pyforms.controls import ControlDateTime
from resources.models import ResourceAccess
from confapp import conf
from django.utils import timezone

class ResourceAccessFormWidget(ModelFormWidget):

    TITLE = "Resource access"
    MODEL = ResourceAccess

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    READ_ONLY = ['resource', 'user', 'start_date', 'end_date']

    FIELDSETS = [
        'resource',
        ('start_date', 'end_date', 'user'),
        ' '
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        obj = self.model_object


        self._revokebtn = ControlButton(
            'Revoke access',
            default=self.__revoke_btn_evt,
            css='red',
            label_visible=False,
            visible=(obj.end_date is None or obj.end_date>=timezone.now().date())
        )

    def __revoke_btn_evt(self):
        self.message_popup(
            'You sure you want to revoke the access',
            'Confirmation',
            buttons=['Confirm', 'Cancel'],
            handler=self.__revoke_evt
        )

    def __revoke_evt(self, popup, button):
        if button=='Confirm':
            access = self.model_object
            access.revoke( PyFormsMiddleware.user() )
            self.end_date.value = access.end_date
            self._revokebtn.hide()
        popup.close()

    def get_buttons_row(self):
        return [no_columns('_cancel_btn', '_revokebtn')]


    def has_update_permissions(self):
        return False

    def has_remove_permissions(self):
        return False




class ResourceAccessCreateForm(ResourceAccessFormWidget):

    READ_ONLY = []

    def __init__(self, *args, **kwargs):
        ModelFormWidget.__init__(self, *args, **kwargs)

    def get_buttons_row(self):
        return ModelFormWidget.get_buttons_row(self)

    def update_object_fields(self, obj):
        obj.created_by = PyFormsMiddleware.user()
        return super().update_object_fields(obj)
