// Fichier qui comporte les routes de l'application

import { Routes, Route, Navigate } from "react-router-dom";
import "./styles/App.css";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import AlreadyConnected from "./pages/AlreadyConnected";
import PrivacyPolicy from "./pages/PrivacyPolicy";
import NotFound from "./pages/NotFound";

export default function App() {
  return (
    <div className="appContainer">
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/already-connected" element={<AlreadyConnected />} />
        <Route path="/privacy" element={<PrivacyPolicy />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/*" element={<NotFound />} />
      </Routes>
    </div>
  );
}
