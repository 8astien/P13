# Generated by Django 3.0 on 2024-12-27 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_transfer_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'addresses'},
        ),
    ]
