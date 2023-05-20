# Generated by Django 4.1.7 on 2023-05-13 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_menuitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitems',
            options={'ordering': ('name',), 'verbose_name_plural': 'menu items'},
        ),
        migrations.AddField(
            model_name='menuitems',
            name='icon',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
