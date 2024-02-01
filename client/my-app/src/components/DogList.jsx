import { useState, useEffect } from "react"
import DogCard from "./DogCard"
import { useLoaderData } from "react-router-dom"

export default function DogList() {
  const [dogs, setDogs] = useState([])
  const user = useLoaderData()
  console.log("***", user)

  useEffect(() => {
    fetch("http://127.0.0.1:5555/dogs")
    .then(resp => resp.json())
    .then(data => setDogs(data))
  }, [])

  if (!user.username) {
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