import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.mark.django_db
def test_index_view_status_code():
    """
    Vérifie que la vue index renvoie un code HTTP 200
    et utilise bien le template 'profiles/index.html'.
    """
    client = Client()
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200

    # Vérifier le template utilisé
    template_names = [t.name for t in response.templates if t.name is not None]
    assert 'profiles/index.html' in template_names


@pytest.mark.django_db
def test_index_view_context():
    """
    Vérifie que la vue index inclut bien la liste des profils dans le contexte.
    """
    # Créons des utilisateurs et leurs profils
    user1 = User.objects.create_user(username='alice', password='pwd123')
    profile1 = Profile.objects.create(user=user1, favorite_city='Paris')

    user2 = User.objects.create_user(username='bob', password='pwd123')
    profile2 = Profile.objects.create(user=user2, favorite_city='Berlin')

    client = Client()
    url = reverse('profiles:index')
    response = client.get(url)

    assert 'profiles_list' in response.context
    profiles_list = response.context['profiles_list']
    # On s'assure que nos deux profils de test sont présents
    assert profile1 in profiles_list
    assert profile2 in profiles_list


@pytest.mark.django_db
def test_profile_view_status_code():
    """
    Vérifie que la vue profile renvoie un code HTTP 200
    et le bon template pour un username existant.
    """
    user = User.objects.create_user(username='charlie', password='pwd123')
    profile = Profile.objects.create(user=user, favorite_city='Rome')

    client = Client()
    url = reverse('profiles:profile', kwargs={'username': 'charlie'})
    response = client.get(url)
    assert response.status_code == 200

    template_names = [t.name for t in response.templates if t.name is not None]
    assert 'profiles/profile.html' in template_names


@pytest.mark.django_db
def test_profile_view_context():
    """
    Vérifie que la vue profile inclut bien l'instance Profile
    attendue dans le contexte.
    """
    user = User.objects.create_user(username='david', password='pwd123')
    profile = Profile.objects.create(user=user, favorite_city='Tokyo')

    client = Client()
    url = reverse('profiles:profile', kwargs={'username': 'david'})
    response = client.get(url)

    assert 'profile' in response.context
    assert response.context['profile'] == profile

@pytest.mark.django_db
def test_profile_model_str():
    """
    Vérifie le __str__ du modèle Profile, qui doit renvoyer le nom d'utilisateur.
    """
    user = User.objects.create_user(username='eve', password='pwd123')
    profile = Profile.objects.create(user=user, favorite_city='Sydney')

    assert str(profile) == 'eve'
