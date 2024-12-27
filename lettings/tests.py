import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view_status_code():
    """
    Test que la vue index renvoie un code HTTP 200 et utilise le bon template.
    """
    client = Client()
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    # Vérifier le template utilisé
    template_names = [t.name for t in response.templates if t.name is not None]
    assert 'lettings/index.html' in template_names


@pytest.mark.django_db
def test_index_view_context():
    """
    Test que la vue index fournit bien la liste des lettings dans le contexte.
    """
    # Créons quelques objets pour tester
    address1 = Address.objects.create(
        number=123, street="Main St", city="CityA", state="CA",
        zip_code=12345, country_iso_code="USA"
    )
    letting1 = Letting.objects.create(title="Letting A", address=address1)

    address2 = Address.objects.create(
        number=456, street="Second St", city="CityB", state="BB",
        zip_code=67890, country_iso_code="FRA"
    )
    letting2 = Letting.objects.create(title="Letting B", address=address2)

    client = Client()
    url = reverse('lettings:index')
    response = client.get(url)

    # Le contexte doit contenir la liste des Letting
    assert 'lettings_list' in response.context
    lettings_list = response.context['lettings_list']
    assert letting1 in lettings_list
    assert letting2 in lettings_list


@pytest.mark.django_db
def test_letting_view_status_code():
    """
    Test que la vue letting renvoie un code HTTP 200 et utilise le bon template
    pour un letting existant.
    """
    # On crée un Letting de test
    address = Address.objects.create(
        number=10,
        street="Main Street",
        city="TestCity",
        state="TS",
        zip_code=11111,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)

    client = Client()
    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200
    # Vérifier le template utilisé
    template_names = [t.name for t in response.templates if t.name is not None]
    assert 'lettings/letting.html' in template_names


@pytest.mark.django_db
def test_letting_view_context():
    """
    Test que la vue letting fournit bien 'title' et 'address' dans le contexte.
    """
    address = Address.objects.create(
        number=20,
        street="Example Road",
        city="ExampleCity",
        state="EX",
        zip_code=22222,
        country_iso_code="GBR"
    )
    letting = Letting.objects.create(title="Example Letting", address=address)

    client = Client()
    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    assert 'title' in response.context
    assert 'address' in response.context
    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address


@pytest.mark.django_db
def test_letting_model_str():
    """
    Test la méthode __str__() du modèle Letting.
    """
    address = Address.objects.create(
        number=111,
        street="Test Street",
        city="TestCity",
        state="TT",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="My Cool Letting", address=address)
    assert str(letting) == "My Cool Letting"


@pytest.mark.django_db
def test_address_model_str():
    """
    Test la méthode __str__() du modèle Address.
    """
    address = Address.objects.create(
        number=999,
        street="Mystery Ave",
        city="Gotham",
        state="GT",
        zip_code=10101,
        country_iso_code="USA"
    )
    assert str(address) == "999 Mystery Ave"
