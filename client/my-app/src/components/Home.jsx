import { useOutletContext } from "react-router-dom"

export default function Home() {
  // const [user] = useOutletContext()
  // console.log(user)
  const user = {'username': 'test'}

  return (
    <>
    <h2>Home Page</h2>
    {user && user.username ? <p>Welcome {user.username}!</p> : null}
    </>
  )
}