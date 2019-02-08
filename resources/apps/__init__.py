from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    name = 'resources'
    # verbose_name = 'Resource Management'

    def ready(self):
        # Import PyForms apps
        from .resources.access import ResourceAccessList
        from .dashboard import DashboardApp
        from .buildings.list import BuildingsListWidget
        from .areas.list import AreasListWidget
        from .rooms.list import RoomsListWidget
        from .equipments import EquipmentListWidget
        from .resources.access_request import AccessRequestList

        #  and place them in the global scope
        global ResourceAccessList
        global DashboardApp
        global BuildingsListWidget
        global AreasListWidget
        global RoomsListWidget
        global EquipmentListWidget
        global AccessRequestList
