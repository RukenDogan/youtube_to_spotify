import Header from "../components/Header";
import PlaylistForm from "../components/PlaylistForm";
import Footer from "../components/Footer";
import "../styles/App.css";

export default function Dashboard() {
  return (
    <div className="appContainer">
      <Header />
      <PlaylistForm />
      <Footer />
    </div>
  );
}
