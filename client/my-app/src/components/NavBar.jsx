import { NavLink } from "react-router-dom";
import "./NavBar.css";

export default function NavBar() {
  return (
    <nav>
      <NavLink to="/" className="nav-link">
        Home
      </NavLink>
      <NavLink to="/dogs" className="nav-link">
        Dogs
      </NavLink>
      <NavLink to="/owners" className="nav-link">
        Owners
      </NavLink>
      <NavLink to="/new-dog" className="nav-link">
        New Dog
      </NavLink>
    </nav>
  );
};