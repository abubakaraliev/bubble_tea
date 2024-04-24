import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from 'react-router-dom';

export default function Form() {
    let navigate = useNavigate();
    const [product, setProduct] = useState()

    function handleSubmit(event) {
        event.preventDefault();
        const name = document.getElementById('name').value
        const price = document.getElementById('price').value
        setProduct({ identifier: name, price: parseFloat(price).toFixed(2) })
        axios.post("http://localhost:8000/products/", {
            identifier: name,
            price: parseFloat(price).toFixed(2),
        }).then((response) => {
            console.log(response);
            navigate('/shop/');
        }).catch((error) => {
            console.error({ error });
        })
    }

    useEffect(() => {
        console.log(product)
    }, [product])
    return (
        <>
            <div class="container w-50 p-5 my-5 border border-1 bg-light">
                <form onSubmit={(e) => handleSubmit(e)}>
                    <fieldset>
                        <h3 class="mb-5 text-center">Formulaire - Nouveau Produit</h3>
                        <label for="name" class="form-label">Nom du produit</label>

                        <div class="mb-3">
                            <input type="text" class="form-control" id="name" required />
                        </div>
                        <label for="price" class="form-label d-flex">Prix</label>
                        <div class="mb-5 input-group">
                            <input type="number" class="form-control" id="price" step="any" required />
                            <span class="input-group-text">€</span>
                        </div>
                        <div class="mb-3 text-center">
                            <button class="btn btn-primary btn-lg">Ajouter</button>
                        </div>
                    </fieldset>
                </form>
            </div >
        </>
    )
}