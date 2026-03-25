import { useState } from "react";
import { syncPlaylist } from "../api/api";
import ResultBox from "./ResultBox";
import { youtubeSchema } from "../schemas/youtube.schema";
import "../styles/PlaylistForm.css";

export default function PlaylistForm() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const trimmedUrl = url.trim();

    const validation = youtubeSchema.safeParse({
      youtube_url: trimmedUrl,
    });

    if (!validation.success) {
      setError(validation.error.issues[0].message);
      setResult(null);
      return;
    }

    try {
      setError(null);
      setLoading(true);

      const data = await syncPlaylist(trimmedUrl);

      if (data?.error) {
        setError(data.error);
        setResult(null);
        return;
      }

      setResult(data);
    } catch (err) {
      setError("Une erreur inattendue est survenue.");
      setResult(null);
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <p className="text">
        Collez l'URL d'une playlist YouTube pour la synchroniser vers Spotify
      </p>

      <form onSubmit={handleSubmit} className="handleSubmitForm">
        <input
          type="text"
          value={url}
          onChange={(e) => {
            setUrl(e.target.value);
            if (error) setError(null);
          }}
          placeholder="Entrez une URL de playlist YouTube"
          className="input"
        />

        <button
          type="submit"
          disabled={loading}
          className={`submitButton ${loading ? "loading" : ""}`}
        >
          <span>{loading ? "Synchronisation..." : "Synchroniser"}</span>
        </button>
      </form>
      
      {error && <p className="error">{error}</p>}
      {result && <ResultBox result={result} />}
    </>
  );
}