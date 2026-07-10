import { NavLink } from "react-router-dom";
import {
  FaHome,
  FaUsers,
  FaUser,
  FaMapMarkerAlt,
  FaChartBar
} from "react-icons/fa";
import { MdSportsCricket } from "react-icons/md";

function Sidebar() {
  return (
    <div className="sidebar">

      <h2>🏏 IPL AI</h2>

      <ul>

        <li>
          <NavLink to="/">
            <FaHome /> Dashboard
          </NavLink>
        </li>

        <li>
          <NavLink to="/teams">
            <FaUsers /> Teams
          </NavLink>
        </li>

        <li>
          <NavLink to="/players">
            <FaUser /> Players
          </NavLink>
        </li>

        <li>
          <NavLink to="/matches">
            <MdSportsCricket /> Matches
          </NavLink>
        </li>

        <li>
          <NavLink to="/venues">
            <FaMapMarkerAlt /> Venues
          </NavLink>
        </li>

        <li>
          <NavLink to="/statistics">
            <FaChartBar /> Statistics
          </NavLink>
        </li>

        <li>
          <NavLink to="/detective">
            🕵 AI Detective
          </NavLink>
        </li>

      </ul>

    </div>
  );
}

export default Sidebar;