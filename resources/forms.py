from django import forms

from .models import Floor


class FloorForm(forms.ModelForm):
    """
    Custom form for a Floor where the Resource name is overwritten.
    """

    class Meta:
        model = Floor
        fields = ('level',)
