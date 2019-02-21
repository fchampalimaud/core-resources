from .form import RoomsEditForm


class RoomCreateForm(RoomsEditForm):

    FIELDSETS = [
        ('name', 'building_floor', 'biosafety_level'),
        'description',
        'biosafety_risks'
    ]