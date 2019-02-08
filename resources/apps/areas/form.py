from resources.apps.resources.form import ResourceFormWidget

class AreasEditForm(ResourceFormWidget):

    FIELDSETS = [
        {
            'a:Area': [
                'name',
                'description',
                'rooms',
                'biosafety_risks'
            ],
            'c:Maintenance': 'MaintenanceListWidget',
            'b:Maintenance contracts': 'MaintenanceContractListWidget',
            'a:Images': 'ImagesListWidget'
        }
    ]