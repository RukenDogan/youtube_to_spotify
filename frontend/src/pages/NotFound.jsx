import "../styles/NotFound.css";
import { useNavigate } from "react-router-dom";

export default function NotFound() {
  const navigate = useNavigate();

  const handleHome = () => {
    navigate("/"); // Redirection vers la page d'accueil
  };

  return (
    <div className="notFoundContainer">
      <h1 className="notFoundTitle">404</h1>
      <p className="notFoundText">Oups… la page que vous cherchez n’existe pas !</p>
      <button className="notFoundButton" onClick={handleHome}>
        Retour à l’accueil
      </button>
    </div>
  );
}
