import { useState } from "react"
import { useLoaderData, useOutletContext } from "react-router-dom"

export default function DogForm() {
  const blankForm = {
    'name': '',
    'age': '',
    'type': '',
    'owner_id': null
  }
  const [formData, setFormData] = useState(blankForm)
  const [error, setError] = useState()
  // const [user] = useOutletContext()
  const owners = useLoaderData()

  function handleSubmit(event) {
    event.preventDefault()
    fetch('http://127.0.0.1:5555/pets', { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(resp => {
      if (resp.ok) {
        return resp.json()
      } else {
        return Promise.reject(resp)
      }
    })
    .then(data => console.log(data))
    .catch(resp => resp.json())
    .then(errorData => setError(errorData))
  }

  function handleNameChange(event) {
    setFormData({...formData, 'name': event.target.value})
  }

  function handleAgeChange(event) {
    setFormData({...formData, 'age': parseInt(event.target.value)})
  }

  function handleTypeChange(event) {
    setFormData({...formData, 'type': event.target.value})
  }

  function handleOwnerChange(event) {
    setFormData({...formData, 'owner_id': parseInt(event.target.value)})
  }

  // if (!user || !user.username) {
  //   return <p>Must be logged in to view this page</p>
  // }

  if (!owners) {
    return <p>Loading...</p>
  }

  const errorElement = error ? <p style={{color: 'red'}}>{error.error}</p> : null

  return (
    <>
    {errorElement}
    <form onSubmit={handleSubmit}>
      <label>Name: </label>
      <input name="name" type="text" onChange={handleNameChange} value={formData.name} /><br />
      <label>Age: </label>
      <input name="age" type="number" onChange={handleAgeChange} value={formData.age} /><br />
      <lable>Type: </lable>
      <input name="type" type="text" onChange={handleTypeChange} value={formData.type} /><br />
      <label>Owner: </label>
      <select name="owner" onChange={handleOwnerChange} value={formData.owner_id}>
        <option value=""> -- </option>
        {owners.map(owner => <option key={owner.id} value={owner.id}>{owner.name}</option>)}
      </select><br />
      <input type="submit" />
    </form>
    </>
  )
}