Interfaces de Programmation
===========================

L'application n'a pas d'API REST pour l'instant, mais les points d'entrée principaux sont :

- **/lettings/** : Liste toutes les annonces immobilières.
- **/lettings/<int:id>/** : Détails d'une annonce.
- **/profiles/** : Liste tous les profils.
- **/profiles/<str:username>/** : Détails d'un profil utilisateur.

Chaque URL utilise les vues Django associées pour gérer les requêtes.