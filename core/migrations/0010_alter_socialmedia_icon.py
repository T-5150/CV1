# Generated by Django 5.0.4 on 2024-05-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Icon'),
        ),
    ]
