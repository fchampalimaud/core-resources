# Generated by Django 2.1.4 on 2019-02-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_auto_20190222_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceaccess',
            name='created_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True, verbose_name='Created on'),
        ),
    ]