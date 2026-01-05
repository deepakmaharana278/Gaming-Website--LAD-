import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./Auth/Login";
import Register from "./Auth/Register";
import About from "./pages/About";


function App() {
  return (
    <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/signup" element={<Register/>} />
      <Route path="/about" element={<About/>} />
    </Routes>
  );
}

export default App;
