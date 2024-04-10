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
import { 
  userLoader, 
  dogListLoader, 
  dogDetailsLoader,
  ownersLoader 
} from './loaders.js'
import { createBrowserRouter, RouterProvider } from "react-router-dom"


const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    loader: userLoader,
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
        path: '/dogdetails/:id',
        element: <DogDetails />,
        loader: dogDetailsLoader
      },
      {
        path: '/alldogs',
        element: <DogList />,
        loader: dogListLoader
      },
      {
        path: '/newdog',
        element: <DogForm />,
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
