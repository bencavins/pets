import NavBar from "./components/NavBar"
import { Outlet, useLoaderData } from "react-router-dom"

export default function App() {
  // const user = useLoaderData()

  return (
    <>
      <header>
        <NavBar />
      </header>
      {/* <Outlet context={[user]} /> */}
      <Outlet />
      <p>footer</p>
    </>
  )
}