# Generated by Django 5.1.6 on 2025-04-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_material_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='en_oferta',
            field=models.BooleanField(default=False, verbose_name='En Oferta'),
        ),
        migrations.AddField(
            model_name='material',
            name='precio_oferta',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio en Oferta'),
        ),
        migrations.AlterField(
            model_name='material',
            name='comision',
            field=models.FloatField(default=0, max_length=20, verbose_name='Comisión'),
        ),
    ]
