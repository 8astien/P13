Structure de la Base de Données
===============================

#### Modèles Principaux

1. **Address** :
   - `number` : Numéro de rue (entier).

   - `street` : Rue (chaîne de caractères).

   - `city` : Ville (chaîne de caractères).

   - `state` : État (chaîne de 2 caractères).

   - `zip_code` : Code postal (entier).

   - `country_iso_code` : Code ISO du pays (3 caractères).


2. **Letting** :
   - `title` : Titre de l'annonce (chaîne de caractères).

   - `address` : Lien vers un objet Address (relation OneToOne).


3. **Profile** :
   - `user` : Utilisateur associé (relation OneToOne avec User).

   - `favorite_city` : Ville préférée (chaîne de caractères).
   