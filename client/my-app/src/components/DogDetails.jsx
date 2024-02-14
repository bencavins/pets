import { useLoaderData, useOutletContext } from "react-router-dom"

export default function DogDetails() {
  const [user] = useOutletContext()
  const dog = useLoaderData()

  if (!user.username) {
    return <p>Must be logged in to view this page</p>
  }

  if (!dog) {
    return <p>Loading...</p>
  }

  return (
    <>
      <h2>Name: {dog.name}</h2>
      <p>Age: {dog.age}</p>
      <p>Owner: {dog.owner ? dog.owner.name : "N/A"}</p>
    </>
  )
}