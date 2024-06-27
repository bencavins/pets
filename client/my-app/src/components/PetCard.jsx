import { Link } from "react-router-dom"

export default function DogCard({ id, name, age, type }) {
  return (
    <li>
      <Link to={`/pets/${id}`}><b>{name}</b>, Type: {type}</Link>
    </li>
  )
}