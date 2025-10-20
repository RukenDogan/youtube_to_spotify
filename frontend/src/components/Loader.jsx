import React from "react";
import "../styles/Loader.css";

export default function Loader() {
  return (
    <div className="loader">
      <div className="loader-inner">
        <div className="loader-item"></div>
        <div className="loader-item"></div>
        <div className="loader-item"></div>
        <div className="loader-item"></div>
      </div>
    </div>
  );
}