import { useState } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import "./styles/App.css";


export default function App() {
  const [user, setUser] = useState(null);

  return (
    <div className="appContainer">
      {user ? <Dashboard /> : <Login onLogin={setUser} />}
    </div>
  );
}
