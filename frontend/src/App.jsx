import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./Auth/Login";
import Register from "./Auth/Register";
<<<<<<< Updated upstream

=======
import About from "./pages/About";
import Contact from "./pages/Contact";
import Privacy from "./pages/Privacy";
import TermsConditions from "./pages/TermsConditions";
import Disclaimer from "./pages/Disclaimer";
import Games from "./pages/Games";
import GamePlayer from "./pages/GamePlayer";
>>>>>>> Stashed changes

function App() {
  return (
    <Routes>
<<<<<<< Updated upstream
      <Route path="/" element={<Home/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/signup" element={<Register/>} />
=======
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Register />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/privacy-policy" element={<Privacy />} />
      <Route path="/terms" element={<TermsConditions />} />
      <Route path="/disclaimer" element={<Disclaimer />} />
      <Route path="/games" element={<Games />} />
      <Route path="/game/:id" element={<GamePlayer />} />
      <Route path="/all-games" element={<Games />} />
      <Route path="/trending" element={<Games />} />
>>>>>>> Stashed changes
    </Routes>
  );
}

export default App;
