import "./App.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Sidebar from "./components/sidebar";

import Dashboard from "./pages/dashboard";
import Teams from "./pages/teams";
import Players from "./pages/players";
import Matches from "./pages/matches";
import Venues from "./pages/venues";
import Statistics from "./pages/statistics";

import AIDetective from "./AIDetective";

function App() {

  return (

    <BrowserRouter>

      <div className="container">

        <Sidebar />

        <div className="main">

          <Routes>

            <Route path="/" element={<Dashboard />} />

            <Route path="/teams" element={<Teams />} />

            <Route path="/players" element={<Players />} />

            <Route path="/matches" element={<Matches />} />

            <Route path="/venues" element={<Venues />} />

            <Route path="/statistics" element={<Statistics />} />

            <Route path="/detective" element={<AIDetective />} />

          </Routes>

        </div>

      </div>

    </BrowserRouter>

  );

}

export default App;