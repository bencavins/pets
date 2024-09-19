import { useState, useEffect } from "react";
import { redirect } from "react-router-dom";

export default function Logout() {
  const [isLoggedOut, setIsLoggedOut] = useState()

  useEffect(() => {
    fetch('/api/logout', {
      method: 'DELETE',
      credentials: 'include'
    })
    .then(resp => {
      if (resp.ok) {
        setIsLoggedOut(true)
        // redirect('/')
      } else {
        setIsLoggedOut(false)
      }
    })
  }, [])
  
  return (
    <p>{isLoggedOut ? "Logged out successfully" : "Error logging out"}</p>
  )
}