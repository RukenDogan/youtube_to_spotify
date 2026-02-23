import { Link } from "react-router-dom";
import "../styles/Footer.css";

export default function Footer() {
  return (
    <footer className="footer">
      <p>
        © 2025 BeatSync App -{" "}
        <Link to="/privacy">Politique de confidentialité</Link> -{" "}
        <Link to="/terms">CGU</Link>
      </p>
    </footer>
  );
}