import { useNavigate } from "react-router-dom";
import HistoryPanel from "../components/HistoryPanel";

export default function History() {
  const navigate = useNavigate();

  return (
    <div>
      <button className="historyBtn" onClick={() => navigate("/dashboard")}>
        ← Retour
      </button>

      <HistoryPanel />
    </div>
  );
}