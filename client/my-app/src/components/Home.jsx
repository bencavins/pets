import { useLoaderData } from "react-router-dom"

export default function Home() {
  const user = useLoaderData()

  return (
    <>
    <h2>Home Page</h2>
    {user ? <p>Welcome {user.username}!</p> : null}
    </>
  )
}