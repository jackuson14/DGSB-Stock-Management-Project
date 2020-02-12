# Generated by Django 2.2.7 on 2020-02-12 08:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200212_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spareparts',
            fields=[
                ('spare_parts_id', models.AutoField(primary_key=True, serialize=False)),
                ('spare_parts_name', models.CharField(max_length=30)),
                ('spare_parts_unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('spare_parts_quantity', models.PositiveIntegerField(default=0)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'spare_parts',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(max_length=30)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('vehicle_number_plate', models.CharField(max_length=10)),
                ('vehicle_owner', models.CharField(max_length=30)),
                ('spare_parts_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Spareparts')),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
        migrations.AddField(
            model_name='spareparts',
            name='vehicle_assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vehicle'),
        ),
    ]
