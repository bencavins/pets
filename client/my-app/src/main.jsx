import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Home from './components/Home.jsx'
import DogList from './components/DogList.jsx'
import DogDetails from './components/DogDetails.jsx'
import DogForm from './components/DogForm.jsx'
import Login from './components/Login.jsx'
import Logout from './components/Logout.jsx'
import ErrorPage from './components/ErrorPage.jsx'
import './index.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom"

async function myLoader({ request, params }) {
  const res = await fetch('http://127.0.0.1:5555/authorized', {
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

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: '/',
        element: <Home />,
        loader: myLoader
      },
      {
        path: '/login',
        element: <Login />
      },
      {
        path: '/logout',
        element: <Logout />
      },
      {
        path: '/dogs/:id',
        element: <DogDetails />
      },
      {
        path: '/dogs',
        element: <DogList />
      },
      {
        path: '/dogs/new',
        element: <DogForm />
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)
