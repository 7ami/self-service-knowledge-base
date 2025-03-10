import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css"; // Keep this for global styles
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "bootstrap/dist/css/bootstrap.min.css"; // Bootstrap for styling
import "bulma/css/bulma.css"; // Bulma for additional styles

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Measure performance in your app if needed
reportWebVitals();
