import { useEffect, useState } from "react"
import { useOutletContext } from "react-router-dom"

export default function Home() {
  const [user, setUser] = useState()
  // console.log(user, setUser)

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
    <>
    <h2>Home Page</h2>
    {user ? <p>Welcome {user.username}</p> : null}
    </>
  )
}