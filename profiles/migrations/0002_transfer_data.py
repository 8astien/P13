from django.db import migrations

def transfer_profile_data(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    for oldprof in OldProfile.objects.all():
        NewProfile.objects.create(
            user=User.objects.get(pk=oldprof.user_id),
            favorite_city=oldprof.favorite_city,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_profile_data, reverse_code=migrations.RunPython.noop),
    ]
