import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_index_view_status_code():
    """
    Test que la page d'accueil (index) renvoie un code HTTP 200.
    """
    client = Client()
    url = reverse('index')  # correspond à path('', index, name='index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_view_template_used():
    """
    Test que la vue index utilise bien le template 'index.html'.
    """
    client = Client()
    url = reverse('index')
    response = client.get(url)
    # On vérifie que 'index.html' fait partie des templates utilisés
    templates_used = [t.name for t in response.templates if t.name is not None]
    assert 'index.html' in templates_used


@pytest.mark.django_db
def test_trigger_error_view():
    """
    Test que la vue 'trigger_error' lève bien une ZeroDivisionError.
    Pour cela, il faut soit avoir un chemin d'URL qui mappe la fonction
    trigger_error, soit on teste la vue directement en l'appelant.
    """
    from oc_lettings_site.views import trigger_error

    with pytest.raises(ZeroDivisionError):
        trigger_error(None)
