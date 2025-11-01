import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";

export default function App() {

  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  );
}




// import { useState } from "react";
// import Login from "./pages/Login";
// import Dashboard from "./pages/Dashboard";
// import "./styles/App.css";
// import Loader from "./components/Loader.jsx";
// import Footer from "./components/Footer.jsx";


// export default function App() {
//   const [user, setUser] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const handleLogin = (userData) => {
//     setLoading(true);
//     setTimeout(() => {
//       setUser(userData);
//       setLoading(false);
//     }, 1500);
//   };

//   return (
//     <div className="appContainer">
//       <div className="content">
//         {loading && <Loader loading={loading} />}
//         {!loading && (user ? <Dashboard /> : <Login onLogin={handleLogin} />)}
//       </div>
//       <Footer />
//     </div>
//   );
// }

