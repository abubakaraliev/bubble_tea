import { Navigate, useOutletContext } from "react-router-dom";
import { redirect } from "react-router-dom";
export default function Order() {
    const [cart, setCart] = useOutletContext();
    if (cart.length < 1) {
        window.location.replace('/shop')
    }
    return (
        <>
            <div class="container text-center">
                <h3 class="my-5">Votre commande</h3>
                <div>
                    <div>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col">Nom</th>
                                    <th scope="col">Prix</th>
                                    <th scope="col">Quantité</th>
                                </tr>
                            </thead>
                            <tbody>
                                {cart.map((item) => (
                                    <tr>
                                        <td>{item.identifier}</td>
                                        <td>{item.price}</td>
                                        <td>{item.quantity}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    <button type="button" class="btn btn-success my-3 bi-bag-check">Valider la commande</button>
                </div>
            </div>
        </>
    )
}