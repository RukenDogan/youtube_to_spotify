import { useState } from "react";

export default function Login() {
  const [loading, setLoading] = useState(false);

  const handleLogin = () => {
    setLoading(true);
    // Ici lancer la redirection vers Spotify OAuth
  };

  return (
    <div>
      <h1>Login Spotify</h1>
      <button onClick={handleLogin}>
        {loading ? "Connexion..." : "Se connecter avec Spotify"}
      </button>
    </div>
  );
}

