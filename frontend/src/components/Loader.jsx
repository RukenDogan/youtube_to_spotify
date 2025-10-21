import React from "react";
import { PacmanLoader } from "react-spinners";
import "../styles/Loader.css";

export default function Loader({ loading }) {
  return (
    <div className="loader-overlay">
      <PacmanLoader 
        color="#eeaac7" 
        loading={loading} 
        size={30} 
        cssOverride={{ opacity: 0.7 }}
        />
    </div>
  );
}
