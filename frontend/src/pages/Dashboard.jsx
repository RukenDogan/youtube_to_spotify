import { useEffect, useState } from "react";
import PlaylistForm from "../components/PlaylistForm";
import "../styles/Dashboard.css";
import logo from "../assets/images/logoBS.png";
import beating from "../assets/images/beating.png";
import Footer from "../components/Footer.jsx";

export default function Dashboard() {
  const [spotifyToken, setSpotifyToken] = useState(null);

  useEffect(() => {
    // Récupère le token stocké côté serveur
    fetch("http://127.0.0.1:5000/token", {
      credentials: "include", // inclut les cookies pour la session
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.access_token) {
          setSpotifyToken(data.access_token);
          localStorage.setItem("spotify_token", data.access_token);
        } else {
          // Si aucun token, redirige vers la page de login
          window.location.href = "/login";
        }
      })
      .catch((err) => {
        console.error("Erreur de récupération du token :", err);
        window.location.href = "/login";
      });
  }, []);

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
