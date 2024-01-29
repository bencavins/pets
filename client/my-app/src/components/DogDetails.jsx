import { useParams } from "react-router-dom"
import { useState, useEffect } from "react"

export default function DogDetails() {
  const { id } = useParams()
  const [dog, setDog] = useState()

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/dogs/${id}`)
    .then(resp => resp.json())
    .then(data => setDog(data))
  }, [])

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