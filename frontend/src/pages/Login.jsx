import "../styles/Login.css";
import logo from "../assets/images/logoBS.png";
import { FaSpotify } from "react-icons/fa";
import Footer from "../components/Footer";

export default function Login({ onLogin }) {
  const handleSpotifyLogin = () => {
    onLogin({ name: "Utilisateur Test" }); // pour simuler une connexion réussie
  };

  return (
    <div className="loginContainer">
      <img src={logo} alt="BeatSync logo" className="loginLogo" />
      <h1 className="loginTitle">Bienvenue sur BeatSync</h1>
      <p className="loginText">
        Connectez votre compte Spotify pour commencer à synchroniser vos playlists YouTube 🎧
      </p>
      <button className="spotifyButton" onClick={handleSpotifyLogin}>
        <FaSpotify className="spotifyIcon" />
        Se connecter avec Spotify
      </button>
    </div>
  );
}

