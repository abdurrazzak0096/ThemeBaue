# Generated by Django 4.2 on 2023-08-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_websitesettings_innerpage_subtitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesettings',
            name='innerPage_Subtitle',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='websitesettings',
            name='main_subtitle',
            field=models.CharField(max_length=250),
        ),
    ]
