import "../styles/Login.css";
import logo from "../assets/images/logoBS.png";
import { FaSpotify } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import Footer from "../components/Footer";

export default function Login() {
  const navigate = useNavigate();
  const handleSpotifyLogin = () => {
    // onLogin({ name: "Utilisateur Test" }); // pour simuler une connexion réussie
      const token = localStorage.getItem("spotify_token"); // ou ta méthode pour savoir si connecté
  if (token) {
    navigate("/already-connected"); // redirection vers la page intermédiaire
  } else {
    window.location.href = "http://127.0.0.1:5000/login"; // redirection vers le backend pour OAuth
    }
  };

  return (
    <div className="loginContainer">
      <img src={logo} alt="BeatSync logo" className="loginLogo" />
      <h1 className="loginTitle">Bienvenue sur BeatSync</h1>
      <p className="loginText">
        Connectez votre compte Spotify pour commencer à synchroniser vos playlists YouTube 🎧
      </p>
      <button type="button" className="spotifyButton" onClick={handleSpotifyLogin}>
        <FaSpotify className="spotifyIcon" />
        Se connecter avec Spotify
      </button>
      <Footer />
    </div>
  );
}

