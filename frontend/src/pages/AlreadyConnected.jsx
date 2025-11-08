import "../styles/AlreadyConnected.css";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import spotifyLogo from "../assets/images/logoBS.png";
import Loader from "../components/Loader.jsx";

export default function AlreadyConnected() {
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate("/dashboard");
    }, 3000); // 3,0 secondes

    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div className="alreadyConnectedContainer">
      <img src={spotifyLogo} alt="Logo" className="alreadyConnectedLogo" />
      <h2 className="alreadyConnectedTitle">Vous êtes déjà connecté à Spotify !</h2>
      <p className="alreadyConnectedText">Redirection vers le dashboard...</p>
      <Loader loading={true} />

    </div>
  );
}