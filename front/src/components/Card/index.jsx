export default function Card({ id, identifier, price, addToCart }) {
    const handleButtonAddCart = e => {
        e.preventDefault();
        let sugar = document.getElementById('sugar');
        addToCart(id, identifier, price, sugar);
    }


    return (
        <>
            <div class="col-md-4">
                <div class="card">
                    <img src="https://via.placeholder.com/150" class="card-img-top" alt="..." />
                    <div class="card-body" id="product" value="test">
                        <h5 class="card-title">{identifier}</h5>
                        <span class="card-text">{price}€</span><br />
                        <label for="customRange1" class="form-label">Quantité de sucre :</label>
                        <input type="range" class="form-range" id="sugar" min="0" max="3" />
                        <button class="btn btn-primary bi-bag-heart" onClick={handleButtonAddCart}> Ajouter au panier</button>
                    </div>
                </div>
            </div>
        </>
    )

}