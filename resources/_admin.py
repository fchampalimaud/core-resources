from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

# from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from .models import Resource
#from .models import SingleResourceAccess
#from .models import MultipleResourceAccess
from .models import Floor
from .models import Room
from .models import Area
from .models import Equipment
from .models import EquipmentCategory
from .models import Image
from .models import EquipmentSection
from .models import Maintenance
from .models import MaintenanceContract

from .forms import FloorForm


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    ...


@admin.register(MaintenanceContract)
class MaintenanceContractAdmin(admin.ModelAdmin):
    filter_horizontal = ('resources', )


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class MaintenanceInline(admin.StackedInline):
    model = Maintenance
    extra = 0
    show_change_link = True

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'notes':
            field.widget.attrs['style'] = 'height: 3em; ' + field.widget.attrs.get('style', '')
        return field


class MaintenanceContractInline(admin.StackedInline):
    model = MaintenanceContract
    extra = 0
    show_change_link = True

"""
class SingleResourceAccessInline(admin.TabularInline):
    fields = ('user', 'start_date', 'end_date')
    model = SingleResourceAccess
    extra = 0

    # readonly_fields = ('status_changed', 'requested_on')
"""

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    ...

"""
@admin.register(SingleResourceAccess)
class SingleResourceAccessAdmin(admin.ModelAdmin):
    ...

# =============================================================================


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):

    form = FloorForm

    inlines = (
        ImageInline,
        # MaintenanceContractInline,
        MaintenanceInline,
        SingleResourceAccessInline,
    )

"""
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'building_floor')
    list_filter = (
        ('building_floor', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ('name', )

    inlines = (
        ImageInline,
        # MaintenanceContractInline,
        MaintenanceInline,
    )


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector')
    search_fields = ('name',)
    list_filter = ('sector', )
    ordering = ('name',)
    filter_horizontal = ('rooms', )

    inlines = (
        ImageInline,
        # MaintenanceContractInline,
        MaintenanceInline,
    )


# =============================================================================

@admin.register(EquipmentCategory)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(EquipmentSection)
class EquipmentRackAdmin(admin.ModelAdmin):

    list_display = ('__str__',)
    list_filter = (
        ('owners', admin.RelatedOnlyFieldListFilter),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['row', 'col']:
            field.widget.attrs['style'] = 'width: 1em; ' + field.widget.attrs.get('style', '')
        return field




class EquipmentRackInline(admin.TabularInline):
    model = EquipmentSection
    extra = 0

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['row', 'col']:
            field.widget.attrs['style'] = 'width: 1em; ' + field.widget.attrs.get('style', '')
        return field


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'maintenance_contracts')
    inlines = (

        ImageInline,
        # MaintenanceContractInline,
        MaintenanceInline,
        EquipmentRackInline,
    )
