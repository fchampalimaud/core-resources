from resources.apps.resources.form import ResourceFormWidget

class AreasEditForm(ResourceFormWidget):

    FIELDSETS = [
        {
            'a:Area': [
                ('name','req_access'),
                'description',
                'rooms',
                'biosafety_risks'
            ],
            'c:Maintenance': 'MaintenanceListWidget',
            'b:Maintenance contracts': 'MaintenanceContractInlineListWidget',
            'a:Images': 'ImagesListWidget'
        }
    ]