# Generated by Django 2.1.4 on 2019-02-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_accessrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrequest',
            name='requested_on',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
    ]