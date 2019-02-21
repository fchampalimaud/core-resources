from resources.apps.resources.form import ResourceFormWidget

class AreasEditForm(ResourceFormWidget):

    FIELDSETS = [
        {
            'a:Area': [
                'name',
                'description',
                'rooms',
                'biosafety_risks',
                'req_access',
                'access_req'
            ],
            'c:Maintenance': 'MaintenanceListWidget',
            'b:Maintenance contracts': 'MaintenanceContractInlineListWidget',
            'a:Images': 'ImagesListWidget'
        }
    ]