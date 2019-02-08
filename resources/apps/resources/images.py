from pyforms_web.widgets.django import ModelAdminWidget
from resources.models import Image


class ImagesListWidget(ModelAdminWidget):
    MODEL = Image
    LIST_DISPLAY = ['image']
    FIELDSETS = ['image']

    TITLE = 'Images'
