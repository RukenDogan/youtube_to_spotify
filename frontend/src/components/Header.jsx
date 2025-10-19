import logo from "../assets/images/logoBS.png";
import beating from "../assets/images/beating.png";
import "../styles/Header.css";

export default function Header() {
  return (
    <>
      <img src={logo} alt="logo" className="positioned-logo" />
      <h1 className="text-h1">
        Synchronisez vos playlists en un battement
        <img src={beating} alt="beating" className="beating" />
      </h1>
    </>
  );
}
