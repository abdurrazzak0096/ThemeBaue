# Generated by Django 4.2 on 2023-08-10 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_rename_type_menu_menu_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dropdownmenu',
            old_name='menu_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='submenu',
            old_name='submenu_type',
            new_name='type',
        ),
    ]
