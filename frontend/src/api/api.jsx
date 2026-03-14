// API pour les routes de l'application

const API_URL = import.meta.env.VITE_API_URL

export async function syncPlaylist(youtubeUrl) {
  try {
    const response = await fetch(`${API_URL}/youtube-to-spotify`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ youtube_url: youtubeUrl }),
      signal: AbortSignal.timeout(600000), // 10 minutes max
      credentials: "include", // gestion des cookies pour le frontend
    });

    if (!response.ok) {
      throw new Error(`Erreur serveur : ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    return { error: error.message };
  }
}

// récupérer l'historique des synchronisations
export async function getHistory() {
  try {
    const response = await fetch(`${API_URL}/history`, {
      method: "GET",
      credentials: "include",
    });

    if (!response.ok) {
      throw new Error(`Erreur serveur : ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    return { error: error.message };
  }
}

export async function getHistoryDetail(runId) {
  try {
    const response = await fetch(`${API_URL}/history/${runId}`, {
      method: "GET",
      credentials: "include",
    });

    if (!response.ok) {
      throw new Error(`Erreur serveur : ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    return { error: error.message };
  }
}