# Generated by Django 4.0.4 on 2022-07-22 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_menu', '0003_bebida_platoprincipal_postre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlatoPrincipal',
            new_name='Plato',
        ),
    ]
