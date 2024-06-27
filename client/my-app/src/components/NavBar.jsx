import { NavLink } from "react-router-dom";
import "./NavBar.css";

export default function NavBar() {

  return (
    <nav>
      <NavLink reloadDocument to="/" className="nav-link">
        Home
      </NavLink>
      <NavLink reloadDocument end to="/pets" className="nav-link">
        Pets
      </NavLink>
      <NavLink reloadDocument to="/owners" className="nav-link">
        Owners
      </NavLink>
      <NavLink reloadDocument to="/pets/new" className="nav-link">
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