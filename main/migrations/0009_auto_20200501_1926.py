# Generated by Django 2.2.7 on 2020-05-01 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200501_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumables',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='fertilizer',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='fungicide',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='herbicide',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='irrigation',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='pesticide',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='spareparts',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='stationery',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='surfacetant',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
        migrations.AddField(
            model_name='tools',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Supplier'),
        ),
    ]
