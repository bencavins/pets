async function userLoader({ request, params }) {
  const res = await fetch('http://127.0.0.1:5555/check_session', {
      method: 'GET',
      credentials: 'include'
    })
    .then(resp => {
      if (resp.ok) {
        return resp.json()
      } else {
        return {}
      }
    })
  return res
}

async function petListLoader({ request, params }) {
  const res = await fetch("http://127.0.0.1:5555/pets")
    .then(resp => resp.json())
  return res
}

async function petDetailsLoader({ request, params }) {
  const res = await fetch(`http://127.0.0.1:5555/pets/${params.id}`)
    .then(resp => resp.json())
  return res
}

async function ownersLoader({ request, params }) {
  const res = await fetch(`http://127.0.0.1:5555/owners`)
    .then(resp => resp.json())
  return res
}

export {
  userLoader, 
  petListLoader,
  petDetailsLoader,
  ownersLoader
}