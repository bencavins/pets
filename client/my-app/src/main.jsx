import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Home from './components/Home.jsx'
import DogList from './components/DogList.jsx'
import DogDetails from './components/DogDetails.jsx'
import ErrorPage from './components/ErrorPage.jsx'
import './index.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom"

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: '/',
        element: <Home />
      },
      {
        path: '/dogs/:id',
        element: <DogDetails />
      },
      {
        path: '/dogs',
        element: <DogList />
      },
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)
