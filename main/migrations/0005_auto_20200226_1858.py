# Generated by Django 2.2.7 on 2020-02-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_consumables_fertilizer_fungicide_herbicide_irrigation_pesticide_stationery_surfacetant_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasing',
            name='purchasing_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='purchasing',
            table='Purchasing',
        ),
    ]
