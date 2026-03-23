## Deployment Guide - BeatSync

### 1. Prérequis

Avant le déploiement, il est nécessaire de disposer :

- d’un compte Render ;
- d’un compte Spotify Developer ;
- d’un compte Google Developer ;
- d’un projet structuré en deux dossiers distincts : `backend` (Flask) et `frontend` (React/Vite) ;
- des variables d’environnement nécessaires au fonctionnement de l’application.

Le backend repose sur Flask, SQLAlchemy et Alembic pour la gestion des migrations.
Le frontend repose sur React et Vite.
Le déploiement présenté ici correspond à l’architecture retenue pour BeatSync sur Render.

---

### 2. Création de la base de données PostgreSQL

La première étape consiste à créer une base de données PostgreSQL sur Render.

Une fois la base créée, Render fournit automatiquement une variable d’environnement `DATABASE_URL`.
Cette URL doit être récupérée puis utilisée dans la configuration du backend afin de permettre la connexion à la base de données.

Cette étape doit être réalisée avant le déploiement du backend, car celui-ci dépend de la base relationnelle pour enregistrer l’historique des synchronisations.

---

### 3. Configuration des variables d’environnement

Le backend nécessite les variables suivantes :

- `SPOTIFY_CLIENT_ID`
- `SPOTIFY_CLIENT_SECRET`
- `SPOTIFY_REDIRECT_URI`
- `YOUTUBE_API_KEY`
- `DATABASE_URL`
- `FRONTEND_URL`
- `FLASK_SECRET_KEY`

Le frontend nécessite notamment :

- `VITE_API_URL`

Ces variables doivent être configurées directement dans l’environnement d’hébergement (ex : Render).

---

### 4. Déploiement du backend

Le backend est déployé sur Render en tant que **Web Service**.

Configuration principale :

- **Root Directory** : `backend`
- présence du fichier `requirements.txt` (dépendances Python)
- présence du dossier `migrations` (gestion des migrations Alembic)
- commande de démarrage : `gunicorn app:app`

Le backend doit être relié à la variable `DATABASE_URL` fournie par la base PostgreSQL créée précédemment.

Après déploiement, il est recommandé de vérifier :

- le bon démarrage du service ;
- la connexion à la base de données ;
- le fonctionnement des routes techniques (ex : `/`, `/health`, `/token`).

Si Alembic est exécuté au démarrage, il convient également de vérifier que les migrations sont correctement appliquées.

---

### 5. Déploiement du frontend

Le frontend est déployé sur Render en tant que **Static Site**.

Configuration principale :

- **Root Directory** : `frontend`
- **Build Command** :`npm install && npm run build`
- **Publish Directory** : `dist`

La variable `VITE_API_URL` doit pointer vers l’URL publique du backend déployé.

---

### 6. Configuration complémentaire

Après le déploiement, plusieurs éléments doivent être vérifiés :

- la configuration de CORS côté backend à l’aide de `FRONTEND_URL` ;
- la règle de réécriture du frontend (`/* → /index.html`) ;
- la cohérence entre `SPOTIFY_REDIRECT_URI`, l’URL backend de production et la configuration du tableau de bord Spotify Developer ;
- l’accessibilité des API externes (Spotify et YouTube).

---

### 7. Points de vigilance

Le flux OAuth peut être impacté par les restrictions liées aux cookies cross-site.
Certaines extensions navigateur ou paramètres de confidentialité peuvent bloquer le fonctionnement du parcours d’authentification.

En mode développement Spotify, seuls les utilisateurs ajoutés à l’allowlist peuvent tester l’application.

---

### 8. Améliorations possibles

Plusieurs améliorations peuvent être envisagées :

- dockerisation de l’application ;
- mise en place d’un pipeline CI/CD ;
- unification du domaine frontend/backend ;
- mise en place d’un système de monitoring ;
- amélioration de la gestion de l’authentification en production.

Dans le cadre du projet, le déploiement sur Render a permis de valider le bon fonctionnement de l’application en environnement de production.

Cette étape constitue une base avant la mise en place d’une conteneurisation via Docker, envisagée dans une démarche d’industrialisation et de reproductibilité de l’environnement.

---



#### Conteneurisation de l’application (Docker)

Dans une logique d’industrialisation du projet, la mise en place d’une conteneurisation via Docker a été envisagée.

L’objectif de cette démarche est de standardiser l’environnement d’exécution de l’application en encapsulant le backend et le frontend dans des conteneurs indépendants. Cela permet notamment de garantir la reproductibilité du projet, indépendamment de l’environnement local ou de la plateforme de déploiement.

La conteneurisation repose sur la création de fichiers de configuration (Dockerfile) permettant de définir les dépendances et les étapes de build de chaque service. Une orchestration via Docker Compose peut également être envisagée afin de faciliter le lancement simultané des différents composants de l’application, notamment le backend, le frontend et la base de données.

Cette approche permettrait à terme de simplifier le déploiement de l’application, d’améliorer sa portabilité et de s’inscrire dans une démarche DevOps plus complète.

La mise en œuvre de cette solution constitue une amélioration en cours de réalisation.
