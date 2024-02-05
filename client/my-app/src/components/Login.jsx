import { useState } from "react"
import { useNavigate } from 'react-router-dom'

export default function Login() {
  const [error, setError] = useState()
  const navigate = useNavigate()

  function handleSubmit(event) {
    event.preventDefault()
    const data = {
      'username': event.target.username.value,
      'password': event.target.password.value
    }

    fetch('http://127.0.0.1:5555/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(data)
    })
    .then(resp => {
      if (resp.ok) {
        console.log('logged in!')
        navigate('/')  // redirect
      } else {
        console.log('error logging in!')
        return Promise.reject(resp)
      }
    })
    .catch(resp => resp.json())
    .then(data => setError(data))
  }

  const errorElement = error ? <p style={{color: 'red'}}>{error.error}</p> : null

  return (
    <>
    {errorElement}
    <form onSubmit={handleSubmit}>
      <label>Username: </label>
      <input type="text" name="username" /><br />
      <label>Password: </label>
      <input type="password" name="password" /><br />
      <input type="submit" />
    </form>
    </>
  )
}