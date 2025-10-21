import "../styles/ResultBox.css";

export default function ResultBox({ result }) {
  return (
    <div className="resultBox">
      {result.error ? (
        <p className="resultError">Erreur : {result.error}</p>
      ) : (
        <>
          <p className="resultText">{result.message}</p>
          <p>🎧 {result.nb_tracks_added} titres ajoutés</p>
        </>
      )}
    </div>
  );
}