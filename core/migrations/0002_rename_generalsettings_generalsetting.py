# Generated by Django 5.0.4 on 2024-05-20 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralSettings',
            new_name='GeneralSetting',
        ),
    ]