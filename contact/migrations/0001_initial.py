# Generated by Django 5.0.4 on 2024-05-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Name')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='Email')),
                ('subject', models.CharField(blank=True, default='', max_length=254, verbose_name='Subject')),
                ('message', models.TextField(blank=True, default='', verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ('name',),
            },
        ),
    ]
