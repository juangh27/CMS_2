# Generated by Django 4.1.7 on 2023-05-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_alter_menuitems_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='icon',
            field=models.CharField(max_length=255),
        ),
    ]
