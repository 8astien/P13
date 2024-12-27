from django.db import migrations

def transfer_address_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('lettings', 'Address')

    for address in OldAddress.objects.all():
        NewAddress.objects.create(
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code,
        )

def transfer_letting_data(apps, schema_editor):
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')

    for letting in OldLetting.objects.all():
        NewLetting.objects.create(
            title=letting.title,
            address=NewAddress.objects.get(pk=letting.address_id),
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(transfer_address_data, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(transfer_letting_data, reverse_code=migrations.RunPython.noop),
    ]
