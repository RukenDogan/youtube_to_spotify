import { useState } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import "./styles/App.css";
import Loader from "./components/Loader.jsx";
import Footer from "./components/Footer.jsx";


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
      <div className="content">
        {loading && <Loader loading={loading} />}
        {!loading && (user ? <Dashboard /> : <Login onLogin={handleLogin} />)}
      </div>
      <Footer />
    </div>
  );
}


// import { BrowserRouter, Routes, Route } from "react-router-dom";
// import Login from "./pages/Login.jsx";
// import Dashboard from "./pages/Dashboard.jsx";

// export default function App() {
//   return (
//     <BrowserRouter>
//       <Routes>
//         <Route path="/login" element={<Login />} />
//         <Route path="/dashboard" element={<Dashboard />} />
//       </Routes>
//     </BrowserRouter>
//   );
// }

