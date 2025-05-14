* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Arial', sans-serif;
}

body {
    background-color: #f5f5f5;
    color: #333;
    line-height: 1.6;
}

header {
    background-color: #d32f2f;
    color: white;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
}

.logo h1 {
    font-size: 2rem;
    font-family: 'Georgia', serif;
}

.logo p {
    font-size: 0.8rem;
    opacity: 0.8;
}

nav ul {
    display: flex;
    list-style: none;
}

nav ul li {
    margin-left: 1.5rem;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: opacity 0.3s;
}

nav ul li a:hover {
    opacity: 0.8;
}

.cart-icon {
    position: relative;
    cursor: pointer;
    font-size: 1.5rem;
}

.cart-count {
    position: absolute;
    top: -10px;
    right: -10px;
    background-color: #ffc107;
    color: #333;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.8rem;
    font-weight: bold;
}

.hero {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                url('https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    margin-top: 60px;
}

.hero-content h2 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero-content p {
    font-size: 1.5rem;
    margin-bottom: 2rem;
}

.btn {
    display: inline-block;
    background-color: #ffc107;
    color: #333;
    padding: 0.8rem 1.5rem;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: #ffca28;
}

.menu {
    padding: 4rem 2rem;
    background-color: white;
}

.menu h2, .about h2, .contact h2, .pedidos h2 {
    text-align: center;
    margin-bottom: 2rem;
    font-size: 2.5rem;
    color: #d32f2f;
}

.menu-filters {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.filter-btn {
    background-color: #f5f5f5;
    border: none;
    padding: 0.5rem 1rem;
    margin: 0 0.5rem;
    cursor: pointer;
    border-radius: 5px;
    transition: all 0.3s;
}

.filter-btn.active {
    background-color: #d32f2f;
    color: white;
}

.filter-btn:hover {
    background-color: #e53935;
    color: white;
}

.pizzas-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.pizza-card {
    background-color: #fff;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

.pizza-card:hover {
    transform: translateY(-10px);
}

.pizza-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.pizza-info {
    padding: 1.5rem;
}

.pizza-info h3 {
    margin-bottom: 0.5rem;
    color: #d32f2f;
}

.pizza-info p {
    margin-bottom: 1rem;
    color: #666;
}

.pizza-price {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.price {
    font-weight: bold;
    font-size: 1.2rem;
    color: #d32f2f;
}

.add-to-cart {
    background-color: #ffc107;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.3s;
}

.add-to-cart:hover {
    background-color: #ffca28;
}

.about, .contact {
    padding: 4rem 2rem;
    background-color: #f9f9f9;
}

.about-content {
    display: flex;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    gap: 2rem;
}

.about-content p {
    flex: 1;
    font-size: 1.1rem;
}

.about-content img {
    flex: 1;
    max-width: 50%;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.contact-info {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.contact-info div {
    background-color: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.contact-info h3 {
    color: #d32f2f;
    margin-bottom: 1rem;
}

footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 2rem;
    margin-top: 2rem;
}

.social-icons {
    margin-top: 1rem;
}

.social-icons a {
    color: white;
    margin: 0 0.5rem;
    font-size: 1.5rem;
    transition: color 0.3s;
}

.social-icons a:hover {
    color: #ffc107;
}

.cart-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 2000;
    justify-content: center;
    align-items: center;
}

.cart-content {
    background-color: white;
    padding: 2rem;
    border-radius: 10px;
    width: 90%;
    max-width: 600px;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
}

.close-cart {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 1.5rem;
    cursor: pointer;
}

.cart-items {
    margin: 1.5rem 0;
}

.cart-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
    border-bottom: 1px solid #eee;
}

.cart-item-info {
    flex: 1;
}

.cart-item-actions {
    display: flex;
    align-items: center;
}

.cart-item-actions button {
    background-color: #f5f5f5;
    border: none;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    cursor: pointer;
    margin: 0 0.5rem;
}

.cart-item-actions span {
    width: 30px;
    text-align: center;
}

.remove-item {
    color: #d32f2f;
    margin-left: 1rem;
    cursor: pointer;
}

.cart-total {
    text-align: right;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 2px solid #eee;
}

.checkout-btn {
    background-color: #d32f2f;
    color: white;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    margin-top: 1rem;
    transition: background-color 0.3s;
}

.checkout-btn:hover {
    background-color: #b71c1c;
}

.pedidos {
    padding: 4rem 2rem;
    background-color: white;
}

.pedido-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.pedido-form {
    background-color: #f9f9f9;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.pedido-form h3 {
    margin: 1.5rem 0 1rem;
    color: #d32f2f;
}

.pedido-form select {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
}

.tamanho-options {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.tamanho-options label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
}

.pedido-resumo {
    background-color: #f9f9f9;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#resumo-pedido {
    margin: 1.5rem 0;
}

#resumo-pedido p {
    margin-bottom: 0.5rem;
}

#finalizar-pedido {
    width: 100%;
    margin-top: 2rem;
    background-color: #d32f2f;
    color: white;
}

#finalizar-pedido:hover {
    background-color: #b71c1c;
}

@media (max-width: 768px) {
    header {
        flex-direction: column;
        padding: 1rem;
    }

    nav ul {
        margin-top: 1rem;
    }

    .hero-content h2 {
        font-size: 2rem;
    }

    .hero-content p {
        font-size: 1.2rem;
    }

    .about-content {
        flex-direction: column;
    }

    .about-content img {
        max-width: 100%;
    }

    .pedido-container {
        grid-template-columns: 1fr;
    }
}
