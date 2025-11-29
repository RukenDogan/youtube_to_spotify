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
        Connectez votre compte Spotify pour commencer à synchroniser vos
        playlists YouTube 🎧
      </p>
      <button
        type="button"
        className="spotifyButton"
        onClick={handleSpotifyLogin} // ← ton onClick ici
      >
        <svg
          className="waveSvg"
          viewBox="0 0 100 100"
          preserveAspectRatio="none"
        >
          <path d="M0 50 Q25 40 50 50 T100 50 V100 H0 Z"></path>
        </svg>

        <svg className="spotifyLogo" viewBox="0 0 168 168">
          <path
            fill="currentColor"
            d="M84 0C37.7 0 0 37.7 0 84s37.7 84 84 84 84-37.7 84-84S130.3 0 84 0zm38.4 121.3c-1.2 2-3.8 2.7-5.8 1.5-16-9.8-36.2-12-60.1-6.5-2.3.5-4.6-1-5.1-3.3-.5-2.3 1-4.6 3.3-5.1 26.3-5.9 49.3-3.2 67.6 7.6 2 1.2 2.7 3.8 1.5 5.8zm8.2-18.5c-1.5 2.5-4.7 3.3-7.2 1.8-18.3-11.2-46.2-14.5-67.8-7.8-2.7.8-5.5-.7-6.3-3.4-.8-2.7.7-5.5 3.4-6.3 24.7-7.3 55.3-3.7 76.6 9.2 2.5 1.5 3.3 4.7 1.8 7.2zm.7-20.1c-22-13.1-58.3-14.3-80.1-7.8-3.1.9-6.4-.8-7.3-3.9-.9-3.1.8-6.4 3.9-7.3 24.9-7.4 65.2-6.1 91.1 9.2 2.8 1.7 3.8 5.3 2.1 8.1-1.7 2.8-5.3 3.8-8.1 2.1z"
          />
        </svg>

        <span>Se connecter avec Spotify</span>
      </button>

      {/* <button type="button" className="spotifyButton" onClick={handleSpotifyLogin}>
        <FaSpotify className="spotifyIcon" />
        Se connecter avec Spotify
      </button> */}
      <Footer />
    </div>
  );
}
