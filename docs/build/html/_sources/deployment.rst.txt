Déploiement
============

1. **Docker** :
   - Construisez une image Docker :
     ``docker build -t oc-lettings:latest .``

   - Poussez l'image sur Docker Hub :
     ``docker push <docker-hub-username>/oc-lettings:latest``

2. **Pipeline CI/CD** :
   - Configurez GitHub Actions pour pousser l'image Docker et déployer sur Render.
   - Les modifications sur `main` déclencheront automatiquement le déploiement.

3. **Render** :
   - Configurez le service Render pour tirer l'image Docker depuis Docker Hub.
   - Assurez-vous que les variables d'environnement nécessaires sont configurées :
     - `SECRET_KEY`
     - `SENTRY_DSN`