import { Link } from "react-router-dom"

export default function DogCard({ id, name, age }) {
  return (
    <li>
      <Link to={`/dogs/${id}`}><b>{name}</b>, Age: {age}</Link>
    </li>
  )
}