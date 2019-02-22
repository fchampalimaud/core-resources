from pyforms.basewidget import no_columns, segment
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.widgets.django import ModelViewFormWidget
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms.controls import ControlButton
from pyforms.controls import ControlDateTime
from resources.models import AccessRequest
from confapp import conf

class AccessRequestFormWidget(ModelFormWidget):

    TITLE = "Access request"
    MODEL = AccessRequest

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    READ_ONLY = ['resource', 'requested_by', 'requested_on', 'reason', 'closed_by', 'closed_on']

    FIELDSETS = [
        no_columns('resource', 'requested_by', 'requested_on'),
        'reason',
        'comment',
        no_columns('_until', '_acceptbtn', '_rejectbtn', 'closed_by', 'closed_on')
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resource.field_css='eleven wide'

        self._until     = ControlDateTime('Access until', visible=False)
        self._acceptbtn = ControlButton('Accept', default=self.__accept_evt, css='basic green', visible=False)
        self._rejectbtn = ControlButton('Reject', default=self.__reject_evt, css='red', visible=False)

        req = self.model_object
        if req.is_approved() is None:
            self._acceptbtn.show()
            self._rejectbtn.show()
            self._until.show()
            self.closed_by.hide()
            self.closed_on.hide()
        else:
            self._until.hide()
            self.closed_by.show()
            self.closed_on.show()
            self.comment.readonly = True

    def has_remove_permissions(self):
        return False

    def has_add_permissions(self):
        return False

    def has_update_permissions(self):
        return False

    def __open_access_evt(self):
        pass

    def __accept_evt(self):
        req = self.model_object
        req.comment = self.comment.value
        req.accept(
            PyFormsMiddleware.user(),
            until=self._until.value,
            comment=self.comment.value
        )
        self._acceptbtn.hide()
        self._rejectbtn.hide()
        self._until.hide()
        self.success('The access request was accepted successfully.')
        self.closed_by.show()
        self.closed_on.show()
        self.closed_by.value = str(req.closed_by)
        self.closed_on.value = req.closed_on
        self.comment.readonly = True

    def __reject_evt(self):
        req = self.model_object
        req.comment = self.comment.value
        req.reject(
            PyFormsMiddleware.user(),
            comment=self.comment.value
        )

        self._acceptbtn.hide()
        self._rejectbtn.hide()
        self._until.hide()

        self.alert('The access request was rejected!')
        self.closed_by.show()
        self.closed_on.show()
        self.closed_by.value = str(req.closed_by)
        self.closed_on.value = req.closed_on
        self.comment.readonly = True

    @property
    def title(self):
        obj = self.model_object
        if obj is None:
            return ModelFormWidget.title.fget(self)
        else:
            return str(obj)

    @title.setter
    def title(self, value):
        ModelFormWidget.title.fset(self, value)