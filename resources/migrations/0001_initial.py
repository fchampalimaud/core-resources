# Generated by Django 2.1.5 on 2019-02-07 14:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('humanresources', '0060_auto_20190116_1552'),
        ('supplier', '0032_auto_20190116_1552'),
        ('research', '0008_auto_20190116_1552'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentCategory',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Equipment Category',
                'verbose_name_plural': 'Equipment Categories',
            },
        ),
        migrations.CreateModel(
            name='EquipmentSection',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'row',
                    models.CharField(
                        help_text='1-9',
                        max_length=1,
                        validators=[
                            django.core.validators.RegexValidator(
                                message='Must be a number', regex='^[0-9]$'
                            )
                        ],
                        verbose_name='row',
                    ),
                ),
                (
                    'col',
                    models.CharField(
                        help_text='A-Z',
                        max_length=1,
                        validators=[
                            django.core.validators.RegexValidator(
                                message='Must be a capital letter', regex='^[A-Z]$'
                            )
                        ],
                        verbose_name='column',
                    ),
                ),
                ('owners', models.ManyToManyField(to='research.Group')),
            ],
            options={
                'verbose_name': 'Equipment section',
                'ordering': ('equipment', 'col', 'row'),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'image',
                    models.ImageField(max_length=150, upload_to='resources/images'),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'maintenance_type',
                    models.IntegerField(
                        choices=[
                            (0, 'Corrective'),
                            (1, 'Predictive'),
                            (2, 'Preventive'),
                        ],
                        default=2,
                    ),
                ),
                ('date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('notes', models.TextField(blank=True)),
                (
                    'quote_file',
                    models.FileField(
                        blank=True, upload_to='resources/maintenance/quotes'
                    ),
                ),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='supplier.Supplier',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceContract',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                (
                    'contract_file',
                    models.FileField(
                        blank=True, upload_to='resources/maintenance/contracts'
                    ),
                ),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='supplier.Supplier',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAccess',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Resource Access',
                'verbose_name_plural': 'Resource Accesses',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                (
                    'resource_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='resources.Resource',
                    ),
                )
            ],
            bases=('resources.resource',),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                (
                    'resource_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='resources.Resource',
                    ),
                )
            ],
            bases=('resources.resource',),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                (
                    'resource_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='resources.Resource',
                    ),
                ),
                ('brand', models.CharField(max_length=80)),
                (
                    'product_number',
                    models.CharField(
                        max_length=80, verbose_name='Model / Product Number'
                    ),
                ),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('notes', models.TextField(blank=True)),
                (
                    'uses_external_booking',
                    models.BooleanField(default=False, help_text='e.g. iLab, Agendo'),
                ),
                (
                    'is_missing',
                    models.BooleanField(
                        default=False,
                        help_text='Use the notes field to provide more information.',
                        verbose_name='Out for repair / outreach events',
                    ),
                ),
                ('acquisition_date', models.DateField(blank=True, null=True)),
                (
                    'warranty',
                    models.PositiveSmallIntegerField(
                        blank=True, help_text='years', null=True
                    ),
                ),
                ('disposal_date', models.DateField(blank=True, null=True)),
                (
                    'an',
                    models.CharField(
                        blank=True, max_length=50, verbose_name='Asset Number'
                    ),
                ),
                ('sn', models.CharField(max_length=50, verbose_name='Serial Number')),
                (
                    'sop',
                    models.FileField(
                        blank=True,
                        upload_to='equipment/sop',
                        verbose_name='Standard Operating Procedure',
                    ),
                ),
                (
                    'category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='resources.EquipmentCategory',
                    ),
                ),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='supplier.Supplier',
                    ),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Leave blank for common use equipment.',
                        related_name='equipments',
                        to='research.Group',
                    ),
                ),
            ],
            options={'verbose_name': 'Equipment'},
            bases=('resources.resource',),
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                (
                    'resource_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='resources.Resource',
                    ),
                ),
                ('level', models.SmallIntegerField(unique=True)),
                (
                    'at_building',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='resources.Building',
                    ),
                ),
            ],
            options={'ordering': ('-level',)},
            bases=('resources.resource',),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                (
                    'resource_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='resources.Resource',
                    ),
                ),
                (
                    'biosafety_level',
                    models.IntegerField(
                        choices=[
                            (0, 'N/A'),
                            (1, 'BSL-1'),
                            (2, 'BSL-2'),
                            (3, 'BSL-3'),
                            (4, 'BSL-4'),
                        ],
                        default=0,
                    ),
                ),
                (
                    'building_floor',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='resources.Floor',
                    ),
                ),
            ],
            options={'ordering': ('-building_floor__level', 'name')},
            bases=('resources.resource',),
        ),
        migrations.AddField(
            model_name='resourceaccess',
            name='resource',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='resources.Resource'
            ),
        ),
        migrations.AddField(
            model_name='resourceaccess',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='maintenancecontract',
            name='resources',
            field=models.ManyToManyField(
                related_name='maintenance_contracts', to='resources.Resource'
            ),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='contract',
            field=models.ForeignKey(
                blank=True,
                help_text='Select a Maintenance Contract covering this service.',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='resources.MaintenanceContract',
            ),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='resource',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='resources.Resource'
            ),
        ),
        migrations.AddField(
            model_name='image',
            name='resource',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='resources.Resource'
            ),
        ),
        migrations.AddField(
            model_name='equipmentsection',
            name='equipment',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='resources.Equipment'
            ),
        ),
        migrations.AddField(
            model_name='equipment',
            name='location',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='resources.Room'
            ),
        ),
        migrations.AddField(
            model_name='equipment',
            name='responsible',
            field=models.ForeignKey(
                blank=True,
                help_text='The person you should contact first',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='humanresources.Person',
            ),
        ),
        migrations.AddField(
            model_name='area',
            name='rooms',
            field=models.ManyToManyField(
                blank=True,
                help_text='The rooms assigned to this area. A user with access to this area will have access to its rooms.',
                related_name='areas',
                to='resources.Room',
                verbose_name='rooms',
            ),
        ),
        migrations.AddField(
            model_name='area',
            name='sector',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='subareas',
                to='resources.Area',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='equipmentsection', unique_together={('equipment', 'row', 'col')}
        ),
    ]