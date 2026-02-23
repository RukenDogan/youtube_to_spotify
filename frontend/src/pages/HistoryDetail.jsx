import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getHistoryDetail } from "../api/api";
import "../styles/HistoryPanel.css"; // pour garder le style
import "../styles/HistoryDetail.css";

export default function HistoryDetail() {
  const { runId } = useParams();
  const navigate = useNavigate();

  const [data, setData] = useState(null);
  const [err, setErr] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const load = async () => {
      setLoading(true);
      setErr("");
      const res = await getHistoryDetail(runId);

      if (res?.error) setErr(res.error);
      else setData(res);

      setLoading(false);
    };
    load();
  }, [runId]);

  return (
    <div className="historyPanel">
      <div className="historyHeader">
        <h2 className="historyTitle">
          Détails synchronisation #{runId}
          {data?.playlist_title && (
            <>
              <br />
              Playlist : "{data.playlist_title}"
            </>
          )}
        </h2>
        <button className="historyBtn" onClick={() => navigate("/history")}>
          ← Retour
        </button>
      </div>

      {loading && <p className="historyText">Chargement…</p>}
      {err && <p className="historyError">Erreur : {err}</p>}

      {!loading && !err && data && (
        <>
          <p className="historyText">
            Statut : <strong>{data.status}</strong> - Ajoutés :{" "}
            <strong>{data.added}</strong> - Échoués :{" "}
            <strong>{data.failed}</strong>
          </p>

          <h3 className="historyTitle">
            Morceaux ajoutés
          </h3>
          {data.added_tracks?.length ? (
            <ul className="historyTrackList">
              {data.added_tracks.map((t, idx) => (
                <li key={idx}>
                  {t.artist} - {t.title}
                </li>
              ))}
            </ul>
          ) : (
            <p className="historyTrackList">Aucun morceau ajouté.</p>
          )}

          <h3 className="historyTitle">
            Morceaux non trouvés
          </h3>
          {data.failed_tracks?.length ? (
            <ul className="historyTrackList">
              {data.failed_tracks.map((t, idx) => (
                <li key={idx}>
                  {t.artist ? `${t.artist} - ` : ""}
                  {t.title || t.query}
                </li>
              ))}
            </ul>
          ) : (
            <p className="historyTrackList">Aucun morceau en échec.</p>
          )}
        </>
      )}
    </div>
  );
}