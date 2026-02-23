import "../styles/Legal.css";
import {
  FaGavel,
  FaUserCheck,
  FaShieldAlt,
  FaLock,
  FaBan,
  FaExclamationTriangle,
  FaLink,
  FaEnvelope,
  FaSyncAlt,
} from "react-icons/fa";
import logo from "../assets/images/logoBS.png";

export default function TermsOfUse() {
  return (
    <div className="legalContainer">
      <img src={logo} alt="BeatSync Logo" className="legalLogo" />
      <h1 className="legalTitle">Conditions d’utilisation</h1>

      <p className="legalIntro">
        Ces conditions d’utilisation expliquent les règles essentielles pour utiliser BeatSync.
        En accédant au service, vous acceptez ces conditions.
      </p>

      <div className="legalSection">
        <FaUserCheck className="legalIcon" />
        <div>
          <h2>Objet du service</h2>
          <p>
            BeatSync est une application permettant de synchroniser des playlists YouTube vers Spotify.
            Le service utilise les API officielles de Spotify et YouTube pour récupérer des informations
            et créer une playlist sur Spotify.
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaSyncAlt className="legalIcon" />
        <div>
          <h2>Accès et connexion</h2>
          <p>
            Pour fonctionner, BeatSync nécessite que vous autorisiez l’accès à votre compte Spotify via OAuth.
            Vous pouvez révoquer cet accès à tout moment depuis Spotify (applications connectées).
          </p>
          <ul>
            <li>Vous êtes responsable de l’usage de votre compte Spotify et de vos actions dans l’application.</li>
            <li>BeatSync ne vous demande jamais votre mot de passe Spotify.</li>
          </ul>
        </div>
      </div>

      <div className="legalSection">
        <FaLock className="legalIcon" />
        <div>
          <h2>Utilisation autorisée</h2>
          <p>
            Vous vous engagez à utiliser BeatSync de manière normale et raisonnable, dans le respect
            des règles des plateformes concernées.
          </p>
          <ul>
            <li>Ne pas détourner le service (automatisation abusive, surcharge volontaire, usage malveillant).</li>
            <li>Ne pas tenter d’accéder aux données d’autres utilisateurs.</li>
            <li>Ne pas contourner les limites imposées par les API (quotas, restrictions, etc.).</li>
          </ul>
        </div>
      </div>

      <div className="legalSection">
        <FaExclamationTriangle className="legalIcon" />
        <div>
          <h2>Limites et disponibilité</h2>
          <p>
            BeatSync dépend de services tiers (Spotify et YouTube) et de leur disponibilité.
            Des interruptions, limitations (quotas) ou modifications d’API peuvent empêcher
            certaines synchronisations, temporairement ou durablement.
          </p>
          <p>
            Le service est fourni « tel quel », sans garantie d’absence d’erreurs.
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaShieldAlt className="legalIcon" />
        <div>
          <h2>Responsabilité</h2>
          <p>
            BeatSync met en œuvre des mesures raisonnables pour fonctionner correctement, mais ne peut pas
            garantir que chaque morceau sera retrouvé, ni que la synchronisation sera identique à 100% à la
            playlist d’origine (ex. versions différentes, titres introuvables).
          </p>
          <ul>
            <li>BeatSync n’est pas responsable des contenus disponibles (ou indisponibles) sur Spotify/YouTube.</li>
            <li>BeatSync n’est pas responsable des interruptions dues aux API, quotas ou pannes de services tiers.</li>
          </ul>
        </div>
      </div>

      <div className="legalSection">
        <FaLink className="legalIcon" />
        <div>
          <h2>Services tiers et affiliation</h2>
          <p>
            BeatSync n’est pas affilié, approuvé ou sponsorisé par Spotify ou YouTube.
            Les noms et logos de services tiers sont la propriété de leurs détenteurs respectifs.
          </p>
          <p>
            L’utilisation de Spotify et YouTube est soumise à leurs propres conditions d’utilisation
            et politiques de confidentialité.
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaBan className="legalIcon" />
        <div>
          <h2>Suspension ou arrêt du service</h2>
          <p>
            En cas d’abus ou d’utilisation contraire à ces conditions, l’accès au service peut être limité
            ou suspendu. BeatSync peut également évoluer, être modifié ou interrompu à tout moment.
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaGavel className="legalIcon" />
        <div>
          <h2>Modifications des conditions</h2>
          <p>
            Ces conditions peuvent être mises à jour. La version publiée sur cette page fait foi.
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaEnvelope className="legalIcon" />
        <div>
          <h2>Contact</h2>
          <p>
            Pour toute question :{" "}
            <a href="mailto:beat20sync25app@gmail.com">
              beat20sync25app@gmail.com
            </a>
          </p>
        </div>
      </div>

      <p className="legalFooter">© 2025 BeatSync. Tous droits réservés.</p>
    </div>
  );
}