import { Link } from "react-router-dom"
export default function Basket({ items, total }) {
    return (
        <>
            <div class="w-25 border border-2">
                <div class="text-center p-3">
                    <span class="fs-3 ">Votre panier</span>
                </div>
                <div class="text-center p-3">
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
                                {items.map((item) => (
                                    <tr>
                                        <td>{item.identifier}</td>
                                        <td>{item.price}</td>
                                        <td>{item.quantity}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>

                </div>
                <div class="text-center">
                    {items.length > 0 ? <Link to='/order' class="btn btn-success bi-bag-check"> Valider le panier</Link> : ''}
                </div>
                <div class="text-center p-3">
                    <span class="fs-5">Total : {total.toFixed(2)}€</span>
                </div>
            </div >
        </>
    )
}