import NavBar from "./components/NavBar"
import { Outlet } from "react-router-dom"

export default function App() {
  return (
    <>
      <header>
        <NavBar />
      </header>
      <Outlet />
      <p>footer</p>
    </>
  )
}