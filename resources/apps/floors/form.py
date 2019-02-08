from pyforms_web.organizers import segment
from resources.apps.rooms import RoomsListWidget
from resources.apps.resources.form import ResourceFormWidget


class FloorsEditForm(ResourceFormWidget):


    INLINES = [
        RoomsListWidget
    ]

    FIELDSETS = [
        ('name', 'level'),
        'description',
        segment(
            'RoomsListWidget',
            css='red'
        )
    ]