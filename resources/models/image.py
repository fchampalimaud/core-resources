from django.db import models


class Image(models.Model):

    image = models.ImageField(upload_to='resources/images', max_length=150)

    resource = models.ForeignKey(to='resources.Resource', on_delete=models.CASCADE)
