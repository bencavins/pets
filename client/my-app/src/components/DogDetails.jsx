import { useLoaderData, useParams } from "react-router-dom"
import { useState, useEffect } from "react"

export default function DogDetails() {
  const { id } = useParams()
  const [dog, setDog] = useState()
  const user = useLoaderData()

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/dogs/${id}`)
    .then(resp => resp.json())
    .then(data => setDog(data))
  }, [])

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