import { Link, Outlet } from "react-router-dom";
import { useState } from "react";
export default function Nav() {
    const [cart, setCart] = useState([])
    return (
        <>
            <div class="d-flex justify-content-between p-3 border border-2">
                <div class="fs-3">Bubble My Tea</div>
                <div>
                    <Link to="/shop" class="me-2 btn btn-primary bi bi-house-door"> Accueil</Link>
                    <Link to="/newProduct" class="me-2 btn btn-danger bi bi-plus-square"> Nouveau Produit</Link>
                    <span class="btn btn-primary bi bi-person" onClick={e => window.location.replace('http://localhost:8000/profile')}> Mon profil</span>
                </div >
            </div>
            <Outlet context={[cart, setCart]} />
        </>
    )
}