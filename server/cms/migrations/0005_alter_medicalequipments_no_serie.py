# Generated by Django 4.1.7 on 2023-06-21 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_alter_medicalequipmentdetails_anios_operando_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalequipments',
            name='no_serie',
            field=models.CharField(max_length=50),
        ),
    ]