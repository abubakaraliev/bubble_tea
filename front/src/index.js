import React from 'react';
import ReactDOM from 'react-dom/client';
import Home from './pages/Home';
import Form from './pages/Form/index.jsx';
import ErrorPage from './pages/Error';
import Nav from './components/Nav/index.jsx';
import Order from './pages/Order/index.jsx';
import { createContext, useContext, useState } from 'react';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const CartContext = createContext([])

const router = createBrowserRouter([
  {
    path: "",
    element: <Nav />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "shop/",
        element: <Home />,
      },
      {
        path: "newProduct",
        element: <Form />,
      },
      {
        path: "order/",
        element: <Order />,
      },
    ],

  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <CartContext.Provider>
      <RouterProvider router={router} />
    </CartContext.Provider>
  </React.StrictMode>
);
