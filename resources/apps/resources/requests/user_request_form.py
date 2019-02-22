from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelFormWidget
from resources.models import AccessRequest, Resource, ResourceAccess
from pyforms.basewidget import BaseWidget
from confapp import conf
from pyforms.controls import ControlQueryList
from pyforms.controls import ControlLabel
from pyforms.controls import ControlEmptyWidget


class UserRequestForm(ModelFormWidget):

    TITLE = 'Access request'

    MODEL = AccessRequest

    FIELDSETS = [
        'resource',
        '_requirements',
        'reason'
    ]

    CREATE_BTN_LABEL = '<i class="plus icon"></i> Submit request'
    HAS_CANCEL_BTN_ON_ADD = False
    HAS_CANCEL_BTN_ON_EDIT = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._user_request_app = kwargs.get('user_request_app')

        self._requirements = ControlLabel('Requirements', visible=False)

        self.resource.changed_event = self.__resource_changed_evt


    def __resource_changed_evt(self):

        if self.resource.value:
            resource = Resource.objects.get(pk=self.resource.value)
            self._requirements.value = f'<h3>{resource.name}</h3>{resource.access_req}'
            self._requirements.show()
        else:
            self._requirements.hide()


    def validate_object(self, obj):
        obj.requested_by = PyFormsMiddleware.user()
        return obj

    def save_object(self, obj, **kwargs):
        self._user_request_app.populate_list()
        return super().save_object(obj, **kwargs)

    def delete_event(self):
        res = super().delete_event()
        self._user_request_app.populate_list()
        return res




class UserRequestApp(BaseWidget):

    UID = 'request-access'
    TITLE = 'Request access'

    # Orquestra ===============================================================
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left'
    ORQUESTRA_MENU_ICON = 'key yellow'
    ORQUESTRA_MENU_ORDER = -1

    # =========================================================================

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request_form = UserRequestForm(user_request_app=self)
        self.request_form_id = request_form.uid

        self._editform = ControlEmptyWidget(
            parent=self,
            name='_editform',
            default=request_form
        )

        self._list = ControlQueryList(
            'Requests',
            list_display=['requested_on', 'resource', 'is_closed', 'is_approved'],
            item_selection_changed_event=self.__item_selection_changed_evt
        )

        self._accesses = ControlQueryList(
            'Approved accesses',
            list_display=['resource', 'start_date', 'end_date', 'is_revoked']
        )

        self.formset = [
            '_editform',
            ' ',
            'h3:Your accesses',
            '_accesses',
            'h3:Your requests',
            '_list',
        ]

        self.populate_list()

    def __item_selection_changed_evt(self):
        request_form = PyFormsMiddleware.get_instance(self.request_form_id)

        req = AccessRequest.objects.get(pk=self._list.selected_row_id)

        if req.is_closed():
            if req.is_approved():
                self.success_popup('The request was approved!', 'Approved')
            else:
                if req.comment:
                    self.alert_popup(req.comment, title='Rejected!')
                else:
                    self.alert_popup('No further information was provided.', title='Rejected!')
            request_form.show_create_form()
        else:
            request_form.show_edit_form(
                pk=self._list.selected_row_id
            )


    def populate_list(self):
        self._list.value = AccessRequest.objects.filter(
            requested_by=PyFormsMiddleware.user()
        )

        self._accesses.value = ResourceAccess.objects.filter(
            user=PyFormsMiddleware.user()
        )
