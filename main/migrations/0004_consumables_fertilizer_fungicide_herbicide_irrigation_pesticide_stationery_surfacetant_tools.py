# Generated by Django 3.0.3 on 2020-02-12 09:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200212_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('tool_id', models.AutoField(primary_key=True, serialize=False)),
                ('tool_name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'tools',
            },
        ),
        migrations.CreateModel(
            name='Surfacetant',
            fields=[
                ('surfacetant_id', models.AutoField(primary_key=True, serialize=False)),
                ('surfacetant_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('Purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'surfacetant',
            },
        ),
        migrations.CreateModel(
            name='Stationery',
            fields=[
                ('stationery_id', models.AutoField(primary_key=True, serialize=False)),
                ('stationery_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'stationery',
            },
        ),
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('pesticide_id', models.AutoField(primary_key=True, serialize=False)),
                ('pesticide_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'pesticide',
            },
        ),
        migrations.CreateModel(
            name='Irrigation',
            fields=[
                ('irrigation_id', models.AutoField(primary_key=True, serialize=False)),
                ('irrigation_item_name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'irrigation',
            },
        ),
        migrations.CreateModel(
            name='Herbicide',
            fields=[
                ('herbicide_id', models.AutoField(primary_key=True, serialize=False)),
                ('herbicide_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'herbicide',
            },
        ),
        migrations.CreateModel(
            name='Fungicide',
            fields=[
                ('fungicide_id', models.AutoField(primary_key=True, serialize=False)),
                ('fungicide_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'fungicide',
            },
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('fertilizer_id', models.AutoField(primary_key=True, serialize=False)),
                ('fertilizer_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'fertilizer',
            },
        ),
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('consumables_id', models.AutoField(primary_key=True, serialize=False)),
                ('consumables_name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=100)),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Purchasing')),
            ],
            options={
                'db_table': 'consumables',
            },
        ),
    ]