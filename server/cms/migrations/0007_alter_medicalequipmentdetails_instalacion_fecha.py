# Generated by Django 4.1.7 on 2023-06-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_alter_medicalequipments_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalequipmentdetails',
            name='instalacion_fecha',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de instalación'),
        ),
    ]