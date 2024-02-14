import { NavLink } from "react-router-dom";
import "./NavBar.css";

export default function NavBar() {

  return (
    <nav>
      <NavLink reloadDocument to="/" className="nav-link">
        Home
      </NavLink>
      <NavLink reloadDocument end to="/dogs" className="nav-link">
        Dogs
      </NavLink>
      <NavLink reloadDocument to="/owners" className="nav-link">
        Owners
      </NavLink>
      <NavLink reloadDocument to="/dogs/new" className="nav-link">
        New Dog
      </NavLink>
      <NavLink reloadDocument to="/login" className="nav-link">
        Login
      </NavLink>
      <NavLink reloadDocument to="/logout" className="nav-link">
        Logout
      </NavLink>
    </nav>
  );
};