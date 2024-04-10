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

async function dogListLoader({ request, params }) {
  const res = await fetch("http://127.0.0.1:5555/dogs")
    .then(resp => resp.json())
  return res
}

async function dogDetailsLoader({ request, params }) {
  const res = await fetch(`http://127.0.0.1:5555/dogs/${params.id}`)
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
  dogListLoader,
  dogDetailsLoader,
  ownersLoader
}