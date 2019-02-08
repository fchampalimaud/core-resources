from .form import RoomsEditForm


class RoomCreateForm(RoomsEditForm):

    FIELDSETS = [
        ('name', 'biosafety_level'),
        'description',
        'biosafety_risks'
    ]