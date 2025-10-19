import { useState } from "react";
import { syncPlaylist } from "../api/api";
import ResultBox from "./ResultBox";
import "../styles/PlaylistForm.css";

export default function PlaylistForm() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const data = await syncPlaylist(url);
    setResult(data);
    setLoading(false);
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
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Entrez une URL de playlist YouTube"
          className="input"
        />
        <button type="submit" disabled={loading} className="submitButton">
          {loading ? "Synchronisation..." : "Synchroniser"}
        </button>
      </form>
      {result && <ResultBox result={result} />}
    </>
  );
}
