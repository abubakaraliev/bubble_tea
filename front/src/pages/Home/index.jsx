import Basket from "../../components/Basket";
import Nav from "../../components/Nav";
import Card from "../../components/Card";

import axios from 'axios';

import { useState, useEffect } from "react";
import { useOutletContext } from "react-router-dom";

function Shop() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  const [cart, setCart] = useOutletContext();
  const [total, setTotal] = useState(0);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const response = await axios.get('http://localhost:8000/products/');
        const data = response.data;
        setProducts(data);
      } catch (err) {
        console.log(err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  const addToCart = (id, identifier, price, sugar) => {
    if (cart.find((cartItem) => cartItem.id === id)) {
      setCart(
        cart.map((cartItem) => cartItem.id === id
          ? { ...cartItem, "quantity": cartItem.quantity + 1 }
          : cartItem // otherwise, return the cart item
        ))
    } else {
      setCart([...cart, { "id": id, "identifier": identifier, "price": price, "quantity": 1, "sugar": sugar }]);
    }

    setTotal(total + Number(price));
  }

  return (
    <>
      <div class="d-flex">
        <Basket items={cart} total={total} />
        <div class="w-75 mx-auto row">
          {loading &&
            <div class="d-flex justify-content-center p-5">
              <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </div>}
          {products.map((product) => (
            <Card key={product.id} id={product.id} identifier={product.identifier} price={product.price} addToCart={addToCart} />
          ))}
        </div>
      </div >
    </>
  )
}

export default Shop;
