import React from "react";
import "../styles/PrivacyPolicy.css";
import { FaShieldAlt, FaLock, FaUserCheck, FaEnvelope } from "react-icons/fa";
import logo from "../assets/images/logoBS.png";
import Footer from "../components/Footer";

export default function PrivacyPolicy() {
  return (
    <div className="privacyContainer">
      <img src={logo} alt="BeatSync Logo" className="privacyLogo" />
      <h1 className="privacyTitle">Politique de confidentialité</h1>
      <p className="privacyIntro">
        BeatSync respecte votre vie privée et protège vos données personnelles.
        Cette page explique comment nous collectons, utilisons et sécurisons vos informations.
      </p>

      <div className="privacySection">
        <FaUserCheck className="privacyIcon" />
        <div>
          <h2>Données collectées</h2>
          <p>
            Nous utilisons uniquement ce qui est nécessaire pour synchroniser vos playlists YouTube vers Spotify : 
            token Spotify OAuth et titres/artistes des vidéos.
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaLock className="privacyIcon" />
        <div>
          <h2>Sécurité</h2>
          <p>
            Toutes les communications passent par HTTPS. Les données sensibles sont protégées et stockées de façon sécurisée.
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaShieldAlt className="privacyIcon" />
        <div>
          <h2>Conservation des données</h2>
          <p>
            Les tokens Spotify expirent automatiquement. Les données sont utilisées uniquement le temps nécessaire à la synchronisation.
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaEnvelope className="privacyIcon" />
        <div>
          <h2>Contact</h2>
          <p>
            Pour toute question : <a href="mailto:à_venir"> adresse mail à venir</a>
          </p>
        </div>
      </div>

      <p className="privacyFooter">© 2025 BeatSync. Tous droits réservés.</p>
      <Footer />
    </div>
  );
}
