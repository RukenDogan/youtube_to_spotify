>
> # Architecture - BeatSync
>
> ## Vue globale
>
> L’application repose sur une architecture découplée :
>
> - Frontend : React (Vite)
> - Backend : Flask (API REST)
> - Base de données : PostgreSQL
> - APIs externes : Spotify, YouTube
>
> ## Backend
>
> Architecture en couches :
>
> - Controllers : gestion des requêtes HTTP
> - Services : logique métier
> - Models : intégration API
> - SQL Models : ORM PostgreSQL
>
> ## Flux principal
>
> 1. L’utilisateur se connecte via Spotify (OAuth)
> 2. Le frontend envoie une URL YouTube
> 3. Le backend extrait les morceaux via YouTube API
> 4. Recherche sur Spotify
> 5. Création de playlist + ajout des morceaux
> 6. Stockage des résultats en base
>
> ## Points critiques
>
> - OAuth (tokens, refresh)
> - Correspondance musique (matching)
> - Communication frontend/backend (CORS, cookies)
