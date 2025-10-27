import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import Header from "../components/Header";
import PlaylistForm from "../components/PlaylistForm";
import "../styles/App.css";

export default function Dashboard() {
  const location = useLocation();
  const [spotifyToken, setSpotifyToken] = useState(null);

  useEffect(() => {
    // Récupère le token depuis l'URL si présent
    const query = new URLSearchParams(location.search);
    const token = query.get("token");
    if (token) {
      setSpotifyToken(token);
      // Stocke le token dans le localStorage pour la connexion ultérieure
      localStorage.setItem("spotify_token", token);
      // Supprime le token de l'URL pour plus de propreté
      window.history.replaceState({}, document.title, "/dashboard");
    }
  }, [location]);

  return (
    <div className="appContainer">
      <Header />
      <PlaylistForm spotifyToken={spotifyToken} />
    </div>
  );
}


// import Header from "../components/Header";
// import PlaylistForm from "../components/PlaylistForm";
// import Footer from "../components/Footer";
// import "../styles/App.css";

// export default function Dashboard() {
//   return (
//     <div className="appContainer">
//       <Header />
//       <PlaylistForm />
//     </div>
//   );
// }
