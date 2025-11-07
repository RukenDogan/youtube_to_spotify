import "../styles/AlreadyConnected.css";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function AlreadyConnected() {
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate("/dashboard");
    }, 2500); // 2,5 secondes

    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Vous êtes déjà connecté à Spotify !</h2>
      <p>Redirection vers le dashboard...</p>
    </div>
  );
}
