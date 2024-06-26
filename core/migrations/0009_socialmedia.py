# Generated by Django 5.0.4 on 2024-05-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('link', models.URLField(blank=True, default='', max_length=254, verbose_name='Link')),
                ('icon', models.ImageField(blank=True, default='', max_length=254, upload_to='', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Media',
                'ordering': ('order',),
            },
        ),
    ]
