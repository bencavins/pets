import NavBar from "./components/NavBar"
import { Outlet } from "react-router-dom"
import { useState, useEffect } from "react"

export default function App() {
  // const [user, setUser] = useState({})

  // useEffect(() => {
  //   console.log('test')
  //   fetch('http://127.0.0.1:5555/authorized')
  //   .then(resp => {
  //     if (resp.ok) {
  //       return resp.json()
  //     }
  //   })
  //   .then(data => setUser(data))
  // }, [])

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