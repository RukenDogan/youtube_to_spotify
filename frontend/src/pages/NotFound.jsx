import { useNavigate } from "react-router-dom";
import "../styles/NotFound.css";


export default function NotFound() {
  const navigate = useNavigate();

  return (
    <div className="notFoundContainer">
      <h1 className="notFoundTitle">404</h1>
      <p className="notFoundText">Page introuvable</p>
      <button className="notFoundButton" onClick={() => navigate("/")}>
        Retour à l'accueil
      </button>
    </div>
  );
}