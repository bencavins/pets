import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";

export default function NavBar() {
  const [user, setUser] = useState()
  
  useEffect(() => {
    fetch('http://127.0.0.1:5555/authorized', {
      method: 'GET',
      credentials: 'include'
    })
    .then(resp => {
      if (resp.ok) {
        return resp.json()
      }
    })
    .then(data => setUser(data))
  }, [])

  return (
    <nav>
      <NavLink reloadDocument to="/" className="nav-link">
        Home
      </NavLink>
      <NavLink end to="/dogs" className="nav-link">
        Dogs
      </NavLink>
      <NavLink to="/owners" className="nav-link">
        Owners
      </NavLink>
      <NavLink to="/dogs/new" className="nav-link">
        New Dog
      </NavLink>
      <NavLink reloadDocument to={user ? "/logout" : "/login"} className="nav-link">
        { user ? "Logout" : "Login"}
      </NavLink>
    </nav>
  );
};