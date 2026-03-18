## Deployment Guide - BeatSync

### 1. Prérequis

* Python 3.11
* Node.js (frontend)
* PostgreSQL
* Compte Spotify Developer
* Compte Render (ou autre plateforme cloud)

---

### 2. Configuration des variables d’environnement

Le backend nécessite les variables suivantes :

* SPOTIFY_CLIENT_ID
* SPOTIFY_CLIENT_SECRET
* SPOTIFY_REDIRECT_URI
* DATABASE_URL
* FRONTEND_URL
* FLASK_SECRET_KEY

Ces variables doivent être configurées dans l’environnement d’hébergement (ex : Render).

---

### 3. Déploiement du backend

* Déployer le dossier `backend`
* Installer les dépendances :

<pre class="overflow-visible! px-0!" data-start="1139" data-end="1178"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install -r requirements.txt</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

* Lancer avec Gunicorn :

<pre class="overflow-visible! px-0!" data-start="1206" data-end="1230"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>gunicorn app:app</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

* Vérifier les routes :
  * `/`
  * `/health`
  * `/token`

---

### 4. Déploiement du frontend

* Déployer le dossier `frontend`
* Commandes de build :

<pre class="overflow-visible! px-0!" data-start="1386" data-end="1419"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>npm install</span><br/><span>npm run build</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

* Dossier de sortie : `dist`

---

### 5. Configuration importante

* Définir `VITE_API_URL` côté frontend
* Vérifier les règles de rewrite (`/* → /index.html`)
* Configurer CORS avec `FRONTEND_URL`

---

### 6. Points de vigilance

* OAuth peut être impacté par les cookies cross-site
* Certaines extensions navigateur (ex : Privacy Badger) peuvent bloquer la connexion
* Les APIs externes (Spotify, YouTube) doivent être accessibles
* En mode développement Spotify, les utilisateurs doivent être ajoutés à l’allowlist

---

### 7. Améliorations possibles

* Dockerisation
* CI/CD
* Domaine unique frontend/backend
* Monitoring avancé
