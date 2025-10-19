import { useState } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import "./styles/App.css";


export default function App() {
  const [user, setUser] = useState(null);

  return (
    <div className="appContainer">
      {user ? <Dashboard /> : <Login onLogin={setUser} />}
    </div>
  );
}





// import { useState } from "react";
// import { syncPlaylist } from "./api/api";
// import "./styles/App.css";
// import logo from "./assets/images/logoBS.png";
// import beating from "./assets/images/beating.png";
// import Login from "./pages/Login";

// export default function App() {
//   const [url, setUrl] = useState("");
//   const [result, setResult] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [user, setUser] = useState(null);


//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     const data = await syncPlaylist(url);
//     setResult(data);
//     setLoading(false);
//   };

//   if (!user) {
//   return <Login onLogin={setUser} />;
// }

//   return ( 
//     <div className="appContainer">
//       <img src={logo} alt="logo" className="logo positioned-logo" />
//       <h1 className="text-h1">
//         Synchronisez vos playlists en un battement
//         <img src={beating} alt="beating" className="beating" />
//       </h1>
//       <p className="text">
//         Collez l'URL d'une playlist YouTube pour la synchroniser vers Spotify
//       </p>
//       <form onSubmit={handleSubmit} className="handleSubmitForm">
//         <input
//           type="text"
//           value={url}
//           onChange={(e) => setUrl(e.target.value)}
//           placeholder="Entrez une URL de playlist YouTube"
//           className="input"
//         />
//         <button
//           type="submit"
//           disabled={loading}
//           className="submitButton"
//         >
//           {loading ? "Synchronisation..." : "Synchroniser"}
//         </button>
//       </form>

//       {result && (
//         <div className="resultBox">
//           {result.error ? (
//             <p className="resultError">Erreur : {result.error}</p>
//           ) : (
//             <>
//               <p className="resultText">{result.message}</p>
//               <p>🎧 {result.nb_tracks_added} titres ajoutés</p>
//             </>
//           )}
//         </div>
//       )}

//       <footer className="footer">
//         <p>© 2025 Ruken Dogan</p>
//       </footer>
//     </div>
//   );
// }
