# Generated by Django 2.1.4 on 2019-02-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20190208_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrequest',
            name='requested_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
