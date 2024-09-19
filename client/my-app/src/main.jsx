import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Home from './components/Home.jsx'
import PetList from './components/PetList.jsx'
import PetDetails from './components/PetDetails.jsx'
import PetForm from './components/PetForm.jsx'
import Login from './components/Login.jsx'
import Logout from './components/Logout.jsx'
import ErrorPage from './components/ErrorPage.jsx'
import './index.css'
import { 
  userLoader, 
  petListLoader, 
  petDetailsLoader,
  ownersLoader 
} from './loaders.js'
import { createBrowserRouter, RouterProvider } from "react-router-dom"


const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    // loader: userLoader,
    children: [
      {
        path: '/',
        element: <Home />
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
        path: '/pets/:id',
        element: <PetDetails />,
        loader: petDetailsLoader
      },
      {
        path: '/pets',
        element: <PetList />,
        loader: petListLoader
      },
      {
        path: '/pets/new',
        element: <PetForm />,
        loader: ownersLoader
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)
