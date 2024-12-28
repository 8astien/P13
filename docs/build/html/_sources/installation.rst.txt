Installation
============

Pour installer le projet localement :

1. Clonez le dépôt : 

``git clone 8astien/P13``

2. Accédez au dossier du projet :

``cd oc_lettings``

3. Installez les dépendances :

``pip install -r requirements.txt``

4. Configurez vos variables d'environnement dans un fichier `.env` :

``SECRET_KEY=votre-clé-app-django``
``SENTRY_DSN=your-sentry-dsn``

5. Appliquez les migrations :

``python manage.py migrate``

6. Lancez le serveur de développement :

``python manage.py runserver``