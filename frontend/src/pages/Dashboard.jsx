import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import PlaylistForm from "../components/PlaylistForm";
import "../styles/Dashboard.css";
import logo from "../assets/images/logoBS.png";
import beating from "../assets/images/beating.png";
import Footer from "../components/Footer.jsx";
import.meta.env.VITE_API_URL

const API_URL = import.meta.env.VITE_API_URL;

export default function Dashboard() {
  const [isSpotifyConnected, setIsSpotifyConnected] = useState(false);
  // const [view, setView] = useState("sync"); 
  const navigate = useNavigate();

  useEffect(() => {
    const checkSpotifyConnected = async () => {
      try {
        const res = await fetch(`${API_URL}/token`, {
          credentials: "include",
        });
        const data = await res.json();

        if (data.connected) {
          setIsSpotifyConnected(true); // token valide, on peut afficher le formulaire
        } else {
          // Pas de token → redirige vers la page NotFound
          navigate("/not-found");
        }
      } catch (err) {
        console.error("Erreur de vérification Spotify :", err);
        navigate("/not-found");
      }
    };

    checkSpotifyConnected();
  }, [navigate]);

  return (
    <div className="dashboardContainer">
      <img src={logo} alt="logo" className="positioned-logo" />
      <h1 className="text-h1">
        Synchronisez vos playlists en un battement
        <img src={beating} alt="beating" className="beating" />
      </h1>

      <nav className="dashNav">
        <button className="dashNavLink" onClick={() => navigate("/history")}>
          Historique
        </button>

        <a
          className="dashNavLink"
          href="https://open.spotify.com/"
          target="_blank"
          rel="noreferrer"
        >
          Ouvrir Spotify
        </a>
      </nav>

      {isSpotifyConnected ? (
        <PlaylistForm />
      ) : (
        <p>Chargement du compte Spotify...</p>
      )}

      <Footer />
    </div>
  );
}
