// src/api.js
export async function syncPlaylist(youtubeUrl) {
  const response = await fetch("http://127.0.0.1:5000/youtube-to-spotify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ youtube_url: youtubeUrl }),
  });

  return response.json();
}
