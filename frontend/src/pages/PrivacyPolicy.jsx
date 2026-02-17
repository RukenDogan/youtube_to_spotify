import React from "react";
import "../styles/PrivacyPolicy.css";
import {
  FaShieldAlt,
  FaLock,
  FaUserCheck,
  FaEnvelope,
  FaDatabase,
  FaGavel,
  FaUserSlash,
} from "react-icons/fa";
import logo from "../assets/images/logoBS.png";

export default function PrivacyPolicy() {
  return (
    <div className="privacyContainer">
      <img src={logo} alt="BeatSync Logo" className="privacyLogo" />
      <h1 className="privacyTitle">Politique de confidentialité</h1>

      <p className="privacyIntro">
        BeatSync respecte votre vie privée et protège vos données personnelles.
        Cette page explique, en termes simples, quelles informations sont
        utilisées, pourquoi, combien de temps, et comment vous gardez le contrôle.
      </p>

      <div className="privacySection">
        <FaUserCheck className="privacyIcon" />
        <div>
          <h2>Données collectées</h2>
          <p>
            BeatSync utilise uniquement les données nécessaires à la
            synchronisation de playlists YouTube vers Spotify :
          </p>
          <ul>
            <li>
              <strong>Token Spotify (OAuth)</strong> : permet d’agir sur votre
              compte Spotify (ex. créer une playlist et ajouter des titres).
            </li>
            <li>
              <strong>Données “musique” minimales</strong> : titre et artiste des
              vidéos, uniquement pour retrouver les morceaux correspondants sur
              Spotify.
            </li>
            <li>
              <strong>Historique de synchronisation</strong> : date, nom de
              playlist, résultat (succès/échec) et message d’erreur simplifié,
              pour vous aider à comprendre ce qui a fonctionné ou non.
            </li>
          </ul>
          <p>
            BeatSync ne vend pas vos données et ne fait pas de publicité ciblée.
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaDatabase className="privacyIcon" />
        <div>
          <h2>Où sont stockées vos données</h2>
          <p>
            Pour assurer le bon fonctionnement de l’application :
          </p>
          <ul>
            <li>
              Les <strong>tokens Spotify</strong> sont stockés dans{" "}
              <strong>MongoDB</strong> (pour éviter de vous reconnecter à chaque
              utilisation).
            </li>
            <li>
              L’<strong>historique utilisateur</strong> est stocké dans une base{" "}
              <strong>SQL</strong> via <strong>SQLAlchemy</strong> (pour afficher
              vos synchronisations passées).
            </li>
          </ul>
        </div>
      </div>

      <div className="privacySection">
        <FaGavel className="privacyIcon" />
        <div>
          <h2>Pourquoi ces données sont utilisées</h2>
          <p>
            Les données sont utilisées uniquement pour :
          </p>
          <ul>
            <li>Exécuter la synchronisation (rechercher et ajouter des titres sur Spotify).</li>
            <li>Afficher un historique compréhensible de vos synchronisations.</li>
            <li>Assurer la sécurité et prévenir les abus (journaux techniques limités).</li>
          </ul>
          <p>
            Conformité : BeatSync applique les principes du{" "}
            <strong>RGPD</strong> (minimisation des données, transparence,
            sécurité et conservation limitée).
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaLock className="privacyIcon" />
        <div>
          <h2>Sécurité</h2>
          <p>
            Nous mettons en place des mesures simples et efficaces pour protéger
            vos informations :
          </p>
          <ul>
            <li>Communications chiffrées via <strong>HTTPS/TLS</strong>.</li>
            <li>
              Accès restreint aux données (seuls les composants nécessaires y
              accèdent).
            </li>
            <li>
              Tokens et secrets gérés de manière sécurisée (pas d’informations
              sensibles “en dur” dans le code).
            </li>
          </ul>
          <p>
            Aucun système n’est infaillible, mais BeatSync limite au maximum les
            données stockées et les accès.
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaShieldAlt className="privacyIcon" />
        <div>
          <h2>Conservation des données</h2>
          <p>
            BeatSync conserve les données uniquement le temps nécessaire :
          </p>
          <ul>
            <li>
              Les <strong>tokens Spotify</strong> peuvent expirer ou être révoqués.
              Ils sont utilisés pour vous permettre de vous reconnecter le moins
              souvent possible.
            </li>
            <li>
              L’<strong>historique</strong> sert à afficher vos synchronisations
              (succès/échecs). Vous pouvez demander sa suppression.
            </li>
          </ul>
          <p>
            Vous pouvez à tout moment reprendre le contrôle (voir “Vos droits”).
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaUserSlash className="privacyIcon" />
        <div>
          <h2>Vos droits (RGPD)</h2>
          <p>
            Conformément au RGPD, vous pouvez demander :
          </p>
          <ul>
            <li>l’accès à vos données,</li>
            <li>la rectification si nécessaire,</li>
            <li>la suppression de vos données,</li>
            <li>l’export de votre historique (si applicable).</li>
          </ul>
          <p>
            Vous pouvez aussi <strong>révoquer l’accès Spotify</strong> à tout
            moment depuis votre compte Spotify (applications connectées). Après
            révocation, BeatSync ne pourra plus synchroniser vos playlists.
          </p>
        </div>
      </div>

      <div className="privacySection">
        <FaEnvelope className="privacyIcon" />
        <div>
          <h2>Contact</h2>
          <p>
            Pour toute question (données, suppression, export) :{" "}
            <a href="mailto:beat20sync25app@gmail.com">
              beat20sync25app@gmail.com
            </a>
          </p>
        </div>
      </div>

      <p className="privacyFooter">© 2025 BeatSync. Tous droits réservés.</p>
    </div>
  );
}
