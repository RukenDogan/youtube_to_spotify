import "../styles/Login.css";
import logo from "../assets/images/logoBS.png";
import Footer from "../components/Footer";
import { FaSpotify } from "react-icons/fa";

export default function Login() {
  const handleSpotifyLogin = () => {
    // onLogin({ name: "Utilisateur Test" }); // pour simuler une connexion réussie
    window.location.href = "http://127.0.0.1:5000/login";
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
    </div>
  );
}

