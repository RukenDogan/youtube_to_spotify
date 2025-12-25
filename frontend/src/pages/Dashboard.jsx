import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import PlaylistForm from "../components/PlaylistForm";
import "../styles/Dashboard.css";
import logo from "../assets/images/logoBS.png";
import beating from "../assets/images/beating.png";
import Footer from "../components/Footer.jsx";
import NotFound from "./NotFound.jsx";

export default function Dashboard() {
  const [spotifyToken, setSpotifyToken] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const checkSpotifyToken = async () => {
      try {
        const res = await fetch("http://127.0.0.1:5000/token", {
          credentials: "include",
        });
        const data = await res.json();

        if (data.access_token) {
          setSpotifyToken(data.access_token);
          localStorage.setItem("spotify_token", data.access_token);
        } else {
          // Pas de token → redirige vers la page NotFound
          navigate("/not-found");
        }
      } catch (err) {
        console.error("Erreur de récupération du token :", err);
        navigate("/not-found");
      }
    };

    checkSpotifyToken();
  }, [navigate]);

  return (
    <div className="dashboardContainer">
      <img src={logo} alt="logo" className="positioned-logo" />
      <h1 className="text-h1">
        Synchronisez vos playlists en un battement
        <img src={beating} alt="beating" className="beating" />
      </h1>
      {spotifyToken ? (
        <PlaylistForm spotifyToken={spotifyToken} />
      ) : (
        <p>Chargement du compte Spotify...</p>
      )}
      <Footer />
    </div>
  );
}
