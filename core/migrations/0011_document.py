# Generated by Django 5.0.4 on 2024-05-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('slug', models.SlugField(blank=True, default='', max_length=254, verbose_name='Slug')),
                ('button_text', models.CharField(blank=True, default='', max_length=254, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, default='', upload_to='documents/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('order',),
            },
        ),
    ]
