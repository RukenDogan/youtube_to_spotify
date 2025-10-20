import { useState } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import "./styles/App.css";
import Loader from "./components/Loader.jsx";


export default function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleLogin = (userData) => {
    setLoading(true);
    setTimeout(() => {
      setUser(userData);
      setLoading(false);
    }, 1500);
  };

  return (
    <div className="appContainer">
      {loading && <Loader />}
      {user ? <Dashboard /> : <Login onLogin={handleLogin} />}
    </div>
  );
}
