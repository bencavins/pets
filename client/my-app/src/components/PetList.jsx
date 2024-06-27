import DogCard from "./PetCard"
import { useLoaderData, useOutletContext } from "react-router-dom"

export default function DogList() {
  // const [user] = useOutletContext()
  const pets = useLoaderData()

  // if (!user || !user.username) {
  //   return <p>Must be logged in to view this page</p>
  // }

  return (
    <>
      <h2>All Pets</h2>
      <ul>
        {pets.map(pet => <DogCard key={pet.id} {...pet} />)}
      </ul>
    </>
  )
}