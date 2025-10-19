export async function syncPlaylist(youtubeUrl) {
  try {
    const response = await fetch("http://127.0.0.1:5000/youtube-to-spotify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ youtube_url: youtubeUrl }),
    });

    if (!response.ok) {
      throw new Error(`Erreur serveur : ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    return { error: error.message };
  }
}
