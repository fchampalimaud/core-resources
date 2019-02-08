from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    name = 'resources'
    # verbose_name = 'Resource Management'

    def ready(self):
        # Import PyForms apps
        from .dashboard import DashboardApp
        from .buildings import BuildingsListWidget
        from .floors import FloorsListWidget
        from .areas import AreasListWidget
        from .rooms import RoomsListWidget
        from .equipments import EquipmentListWidget

        #  and place them in the global scope
        global DashboardApp
        global BuildingsListWidget
        global FloorsListWidget
        global AreasListWidget
        global RoomsListWidget
        global EquipmentListWidget
