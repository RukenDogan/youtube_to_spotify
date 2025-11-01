import { useEffect, useState } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import PlaylistForm from "../components/PlaylistForm";
import "../styles/App.css";

export default function Dashboard() {
  const [spotifyToken, setSpotifyToken] = useState(null);

  useEffect(() => {
    // Récupère le token stocké côté serveur
    fetch("http://localhost:5000/token", { 
      credentials: "include", // inclut les cookies pour la session
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.access_token) {
          setSpotifyToken(data.access_token);
          localStorage.setItem("spotify_token", data.access_token);
        } else {
          // Si aucun token, redirige vers la page de login
          window.location.href = "/";
        }
      })
      .catch((err) => {
        console.error("Erreur de récupération du token :", err);
        window.location.href = "/";
      });
  }, []);

  return (
    <div className="appContainer">
      <Header />
      {spotifyToken ? (
        <PlaylistForm spotifyToken={spotifyToken} />
      ) : (
        <p>Chargement du compte Spotify...</p>
      )}
      <Footer />
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
