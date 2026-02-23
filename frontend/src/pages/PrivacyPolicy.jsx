import React from "react";
import "../styles/Legal.css";
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
    <div className="legalContainer">
      <img src={logo} alt="BeatSync Logo" className="legalLogo" />
      <h1 className="legalTitle">Politique de confidentialité</h1>

      <p className="legalIntro">
        BeatSync respecte votre vie privée et protège vos données personnelles.
        Cette page explique, en termes simples, quelles informations sont
        utilisées, pourquoi, combien de temps, et comment vous gardez le contrôle.
      </p>

      <div className="legalSection">
        <FaUserCheck className="legalIcon" />
        <div>
          <h2>Données collectées</h2>
          <p>
            BeatSync utilise uniquement les données nécessaires à la
            synchronisation de playlists YouTube vers Spotify :
          </p>
          <ul>
            <li>
              <strong>Tokens Spotify (OAuth 2.0 : access + refresh)</strong> : permettent
              d’agir sur votre compte Spotify (ex. créer une playlist et ajouter des titres).
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

      <div className="legalSection">
        <FaDatabase className="legalIcon" />
        <div>
          <h2>Où sont stockées vos données</h2>
          <p>Pour assurer le bon fonctionnement de l’application :</p>
          <ul>
            <li>
              Les <strong>tokens Spotify</strong> sont stockés de manière sécurisée sur nos serveurs,
              afin de permettre la synchronisation sans vous reconnecter à chaque utilisation.
            </li>
            <li>
              L’<strong>historique utilisateur</strong> est stocké dans une base de données dédiée
              afin d’afficher vos synchronisations passées.
            </li>
          </ul>
          <p>
            BeatSync s’appuie sur des <strong>services tiers</strong> (Spotify et YouTube) ainsi que sur
            un <strong>hébergeur</strong> et des services de base de données nécessaires au fonctionnement.
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaGavel className="legalIcon" />
        <div>
          <h2>Pourquoi ces données sont utilisées</h2>
          <p>Les données sont utilisées uniquement pour :</p>
          <ul>
            <li>Exécuter la synchronisation (rechercher et ajouter des titres sur Spotify).</li>
            <li>Afficher un historique compréhensible de vos synchronisations.</li>
            <li>Assurer le bon fonctionnement et la sécurité du service.</li>
          </ul>
          <p>
            Base légale : exécution du service demandé (synchronisation) et intérêt légitime (sécurité).
          </p>
          <p>
            Conformité : BeatSync applique les principes du{" "}
            <strong>RGPD</strong> (minimisation des données, transparence,
            sécurité et conservation limitée).
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaLock className="legalIcon" />
        <div>
          <h2>Sécurité</h2>
          <p>
            Nous mettons en place des mesures simples et efficaces pour protéger
            vos informations :
          </p>
          <ul>
            <li>Communications chiffrées via <strong>HTTPS/TLS</strong>.</li>
            <li>
              L’accès aux données est limité uniquement aux éléments nécessaires au fonctionnement du service.
            </li>
            <li>
              Les informations sensibles (comme les clés d’accès techniques) sont protégées et ne sont jamais exposées publiquement.
            </li>
            <li>
              Les informations de connexion ne sont jamais enregistrées dans votre navigateur.
            </li>
          </ul>
          <p>
            Aucun système n’est infaillible, mais BeatSync limite au maximum les
            données stockées et les accès.
          </p>
        </div>
      </div>

      <div className="legalSection">
        <FaShieldAlt className="legalIcon" />
        <div>
          <h2>Conservation des données</h2>
          <p>BeatSync conserve les données uniquement le temps nécessaire :</p>
          <ul>
            <li>
              Les <strong>tokens Spotify</strong> peuvent expirer ou être révoqués.
              Ils sont conservés tant que la connexion est active, puis supprimés sur demande
              ou après révocation.
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

      <div className="legalSection">
        <FaUserSlash className="legalIcon" />
        <div>
          <h2>Vos droits (RGPD)</h2>
          <p>Conformément au RGPD, vous pouvez demander :</p>
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

      <div className="legalSection">
        <FaEnvelope className="legalIcon" />
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

      <p className="legalFooter">© 2025 BeatSync. Tous droits réservés.</p>
    </div>
  );
}