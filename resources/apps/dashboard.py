from django.conf import settings

from confapp import conf
from pyforms_web.basewidget import BaseWidget
from pyforms_web.controls.control_template import ControlTemplate

from resources.models import Equipment


class DashboardApp(BaseWidget):
    """
    """

    UID = 'resources'
    TITLE = 'Resources'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU = 'middle-left'
    ORQUESTRA_MENU_ICON = 'cubes'
    ORQUESTRA_MENU_ORDER = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._template = ControlTemplate(template='resources/dashboard.html')

        self._template.value = {
            'num_equipments': Equipment.objects.count(),
            'num_unavailable': Equipment.objects.unavailable().count(),
            'num_uncovered': Equipment.objects.uncovered().count(),
            'num_missing_details': Equipment.objects.missing_details().count(),
        }

        self.formset = ['_template']

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True

        if user.groups.filter(name=settings.PROFILE_OPERATIONS_MANAGER).exists():
            return True

        return False
