import { useEffect, useState } from "react";
import { getHistory } from "../api/api";
import { useNavigate } from "react-router-dom";
import "../styles/HistoryPanel.css";

export default function HistoryPanel() {
  const [runs, setRuns] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");
  const navigate = useNavigate();

  const load = async () => {
    setLoading(true);
    setErr("");
    const data = await getHistory();

    if (data?.error) {
      setErr(data.error);
      setRuns([]);
    } else {
      setRuns(data);
    }
    setLoading(false);
  };

  useEffect(() => {
    load();
  }, []);

  return (
    <div className="historyPanel">
      <div className="historyHeader">
        <h2 className="historyTitle">Historique des synchronisations</h2>
        <button className="historyBtn" onClick={load} disabled={loading}>
          Rafraîchir
        </button>
      </div>

      {loading && <p className="historyText">Chargement…</p>}
      {err && <p className="historyError">Erreur : {err}</p>}

      {!loading && !err && runs.length === 0 && (
        <p className="historyText">Aucune synchronisation enregistrée.</p>
      )}

      {!loading && !err && runs.length > 0 && (
        <div className="historyTableWrap">
          <table className="historyTable">
            <thead>
              <tr>
                <th>Date</th>
                <th>Playlist</th>
                <th>Statut</th>
                <th>Ajoutés</th>
                <th>Détails</th>
              </tr>
            </thead>
            <tbody>
              {runs.map((r) => (
                <tr key={r.id}>
                  <td>{new Date(r.started_at).toLocaleString()}</td>
                  <td>{r.playlist_title}</td>
                  <td>
                    <span
                      className={
                        r.status === "SUCCESS"
                          ? "historyBadge success"
                          : "historyBadge failed"
                      }
                    >
                      {r.status}
                    </span>
                  </td>
                  <td>{r.added}</td>
                  <td>
                    <button
                      className="historyBtn"
                      onClick={() => navigate(`/history/${r.id}`)}
                    >
                      Voir
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
