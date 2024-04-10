import DogCard from "./DogCard"
import { useLoaderData, useOutletContext } from "react-router-dom"

export default function DogList() {
  const [user] = useOutletContext()
  const dogs = useLoaderData()

  if (!user || !user.username) {
    return <p>Must be logged in to view this page</p>
  }

  return (
    <>
      <h2>All Dogs (go to heaven?)</h2>
      <ul>
        {dogs.map(dog => <DogCard key={dog.id} {...dog} />)}
      </ul>
    </>
  )
}