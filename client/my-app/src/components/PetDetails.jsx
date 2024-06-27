import { useLoaderData, useOutletContext } from "react-router-dom"

export default function DogDetails() {
  // const [user] = useOutletContext()
  const pet = useLoaderData()

  // if (!user.username) {
  //   return <p>Must be logged in to view this page</p>
  // }

  if (!pet) {
    return <p>Loading...</p>
  }

  return (
    <>
      <h2>Name: {pet.name}</h2>
      <p>Age: {pet.age}</p>
      <p>Type: {pet.type}</p>
      <p>Owner: {pet.owner ? pet.owner.name : "N/A"}</p>
    </>
  )
}