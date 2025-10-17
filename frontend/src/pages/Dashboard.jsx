// import { useState } from "react";
// import { syncPlaylist } from "./api";
// import beating from "./assets/images/beating.png";
// import "./App.css";
// import logo from "/src/assets/images/logoBS.png";

// export default function Dashboard({ logo }) {
//   const [url, setUrl] = useState("");
//   const [result, setResult] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     const data = await syncPlaylist(url);
//     setResult(data);
//     setLoading(false);
//   };

//   return (
//     <div className="dashboardContainer">
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
//         <button type="submit" disabled={loading} className="submitButton">
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
//     </div>
//   );
// }
