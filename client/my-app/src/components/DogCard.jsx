export default function DogCard({ id, name, age }) {
  return (
    <li>
      <p><b>{name}</b>, Age: {age}</p>
    </li>
  )
}