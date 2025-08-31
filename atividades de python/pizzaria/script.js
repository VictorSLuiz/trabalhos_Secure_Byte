const pizzas = [
    {
        id: 1,
        name: "Margherita",
        description: "Molho de tomate, mussarela, manjericão fresco",
        category: "classicas",
        image: "https://images.unsplash.com/photo-1513104890138-7c749659a591?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        id: 2,
        name: "Pepperoni",
        description: "Molho de tomate, mussarela e pepperoni",
        category: "classicas",
        image: "https://images.unsplash.com/photo-1620374645498-af6bd681a0bd?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        id: 3,
        name: "Quatro Queijos",
        description: "Molho de tomate, mussarela, parmesão, gorgonzola e provolone",
        category: "classicas",
        image: "https://images.unsplash.com/photo-1595854341625-f33ee10dbf94?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        id: 4,
        name: "Calabresa",
        description: "Molho de tomate, mussarela e calabresa",
        category: "classicas",
        image: "https://images.unsplash.com/photo-1601924582970-9238bcb495d9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        id: 5,
        name: "Frango com Catupiry",
        description: "Molho de tomate, frango desfiado e catupiry",
        category: "especiais",
        image: "https://images.unsplash.com/photo-1593504049359-74330189a345?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        id: 6,
        name: "Portuguesa",
        description: "Molho de tomate, mussarela, presunto, ovo, cebola e azeitonas",
        category: "especiais",
        image: "https://images.unsplash.com/photo-1588315029754-2dd089d39a1a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        id: 7,
        name: "Brigadeiro",
        description: "Chocolate brigadeiro e granulado",
        category: "doces",
        image: "https://sdmntprcentralus.oaiusercontent.com/files/00000000-f46c-61f5-b89e-a6cce029a497/raw?se=2025-06-03T01%3A28%3A14Z&sp=r&sv=2024-08-04&sr=b&scid=74f6f6e6-c8b0-55ee-9499-1b15e260ae32&skoid=add8ee7d-5fc7-451e-b06e-a82b2276cf62&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-06-02T22%3A57%3A39Z&ske=2025-06-03T22%3A57%3A39Z&sks=b&skv=2024-08-04&sig=8dd8vysw%2By0lhfRaM5vMW8cD3ea1jlnIatlEBBNdkW8%3D"
    },
    {
        id: 8,
        name: "Romeu e Julieta",
        description: "Goiabada e queijo mussarela",
        category: "doces",
        image: "https://sdmntprnorthcentralus.oaiusercontent.com/files/00000000-626c-622f-8adf-02a9736c80c8/raw?se=2025-06-03T01%3A25%3A47Z&sp=r&sv=2024-08-04&sr=b&scid=c05a81c1-30ab-502a-8ca8-c02c22523b7c&skoid=add8ee7d-5fc7-451e-b06e-a82b2276cf62&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-06-02T22%3A58%3A59Z&ske=2025-06-03T22%3A58%3A59Z&sks=b&skv=2024-08-04&sig=jZ4e85BPrJkvhSQhuj5LKhXqvX%2BxdfJXy6ANygF3umQ%3D"
    }
];

let cart = [];
const cartModal = document.querySelector('.cart-modal');
const cartItemsContainer = document.querySelector('.cart-items');
const cartCount = document.querySelector('.cart-count');
const totalPriceElement = document.querySelector('.total-price');
const cartIcon = document.querySelector('.cart-icon');
const closeCartBtn = document.querySelector('.close-cart');
const checkoutBtn = document.querySelector('.checkout-btn');
const filterButtons = document.querySelectorAll('.filter-btn');
const pizzasContainer = document.querySelector('.pizzas-container');

function displayPizzas(category = 'all') {
    pizzasContainer.innerHTML = '';
    
    const filteredPizzas = category === 'all' 
        ? pizzas 
        : pizzas.filter(pizza => pizza.category === category);
    
    filteredPizzas.forEach(pizza => {
        const pizzaCard = document.createElement('div');
        pizzaCard.className = 'pizza-card';
        pizzaCard.innerHTML = `
            <img src="${pizza.image}" alt="${pizza.name}" class="pizza-img">
            <div class="pizza-info">
                <h3>${pizza.name}</h3>
                <p>${pizza.description}</p>
                <div class="pizza-price">
                    <span class="price">R$ ${pizza.price.toFixed(2)}</span>
                    <button class="add-to-cart" data-id="${pizza.id}">Adicionar</button>
                </div>
            </div>
        `;
        pizzasContainer.appendChild(pizzaCard);
    });
    
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', addToCart);
    });
}

function addToCart(e) {
    const pizzaId = parseInt(e.target.getAttribute('data-id'));
    const pizza = pizzas.find(p => p.id === pizzaId);
    
    const existingItem = cart.find(item => item.id === pizzaId);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            ...pizza,
            quantity: 1
        });
    }
    
    updateCart();
}

function updateCart() {
    cartCount.textContent = cart.reduce((total, item) => total + item.quantity, 0);
    localStorage.setItem('cart', JSON.stringify(cart));
}

function displayCart() {
    cartItemsContainer.innerHTML = '';
    
    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p>Seu carrinho está vazio</p>';
        totalPriceElement.textContent = '0.00';
        return;
    }
    
    let totalPrice = 0;
    
    cart.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <div class="cart-item-info">
                <h4>${item.name}</h4>
                <p>R$ ${item.price.toFixed(2)}</p>
            </div>
            <div class="cart-item-actions">
                <button class="decrease">-</button>
                <span>${item.quantity}</span>
                <button class="increase">+</button>
                <span class="remove-item">&times;</span>
            </div>
        `;
        cartItemsContainer.appendChild(cartItem);
        
        totalPrice += item.price * item.quantity;
        
        const decreaseBtn = cartItem.querySelector('.decrease');
        const increaseBtn = cartItem.querySelector('.increase');
        const removeBtn = cartItem.querySelector('.remove-item');
        
        decreaseBtn.addEventListener('click', () => {
            if (item.quantity > 1) {
                item.quantity -= 1;
                displayCart();
                updateCart();
            }
        });
        
        increaseBtn.addEventListener('click', () => {
            item.quantity += 1;
            displayCart();
            updateCart();
        });
        
        removeBtn.addEventListener('click', () => {
            cart = cart.filter(cartItem => cartItem.id !== item.id);
            displayCart();
            updateCart();
        });
    });
    
    totalPriceElement.textContent = totalPrice.toFixed(2);
}

cartIcon.addEventListener('click', () => {
    cartModal.style.display = 'flex';
    displayCart();
});

closeCartBtn.addEventListener('click', () => {
    cartModal.style.display = 'none';
});

checkoutBtn.addEventListener('click', () => {
    if (cart.length > 0) {
        alert('Pedido finalizado com sucesso! Obrigado pela preferência.');
        cart = [];
        updateCart();
        displayCart();
        cartModal.style.display = 'none';
    } else {
        alert('Seu carrinho está vazio!');
    }
});

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        displayPizzas(button.getAttribute('data-category'));
    });
});

window.addEventListener('click', (e) => {
    if (e.target === cartModal) {
        cartModal.style.display = 'none';
    }
});

function loadCart() {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
        updateCart();
    }
}

const precos = {
    pizzas: { P: 20.00, M: 30.00, G: 40.00 },
    bebidas: { coca: 10.00, dolly: 4.00, fanta: 8.00, guarana: 9.00 }
};

const nomes = {
    pizzas: {
        calabresa: 'Calabresa',
        moda: 'A Moda',
        '4queijos': '4 Queijos',
        portuguesa: 'Portuguesa',
        brigadeiro: 'Brigadeiro',
        romeu_e_julieta: 'Romeu e Julieta',
    },
    tamanhos: {
        P: 'Pequena',
        M: 'Média',
        G: 'Grande'
    },
    bebidas: {
        coca: 'Coca-Cola 2L',
        dolly: 'Dolly 1L',
        fanta: 'Fanta 2L',
        guarana: 'Guaraná 2L'
    }
};

const saborPizza = document.getElementById('sabor-pizza');
const tamanhoRadios = document.querySelectorAll('input[name="tamanho"]');
const bebidaSelect = document.getElementById('bebida');
const finalizarBtn = document.getElementById('finalizar-pedido');
const resumoPedido = document.getElementById('resumo-pedido');
const totalPedido = document.getElementById('total-pedido');

function atualizarResumo() {
    const pizza = saborPizza.value;
    const tamanho = document.querySelector('input[name="tamanho"]:checked')?.value;
    const bebida = bebidaSelect.value;
    
    let html = '';
    let total = 0;
    
    if (pizza && tamanho) {
        const nomePizza = nomes.pizzas[pizza];
        const nomeTamanho = nomes.tamanhos[tamanho];
        const precoPizza = precos.pizzas[tamanho];
        
        html += `<p>Pizza ${nomePizza} ${nomeTamanho} - R$ ${precoPizza.toFixed(2)}</p>`;
        total += precoPizza;
    }
    
    if (bebida) {
        const nomeBebida = nomes.bebidas[bebida];
        const precoBebida = precos.bebidas[bebida];
        
        html += `<p>${nomeBebida} - R$ ${precoBebida.toFixed(2)}</p>`;
        total += precoBebida;
    }
    
    if (html === '') {
        html = '<p>Selecione os itens do seu pedido</p>';
    }
    
    resumoPedido.innerHTML = html;
    totalPedido.innerHTML = `<h4>Total: R$ ${total.toFixed(2)}</h4>`;
}

saborPizza.addEventListener('change', atualizarResumo);
tamanhoRadios.forEach(radio => radio.addEventListener('change', atualizarResumo));
bebidaSelect.addEventListener('change', atualizarResumo);

finalizarBtn.addEventListener('click', () => {
    const pizza = saborPizza.value;
    const tamanho = document.querySelector('input[name="tamanho"]:checked')?.value;
    const bebida = bebidaSelect.value;
    
    if (!pizza || !tamanho || !bebida) {
        alert('Por favor, selecione todos os itens do pedido!');
        return;
    }
    
    const nomePizza = nomes.pizzas[pizza];
    const nomeTamanho = nomes.tamanhos[tamanho];
    const nomeBebida = nomes.bebidas[bebida];
    const total = precos.pizzas[tamanho] + precos.bebidas[bebida];
    
    alert(`Pedido finalizado com sucesso!\n\nPizza ${nomePizza} ${nomeTamanho}\n${nomeBebida}\n\nTotal: R$ ${total.toFixed(2)}\n\nObrigado pela preferência!`);
    
    saborPizza.value = '';
    tamanhoRadios.forEach(radio => radio.checked = false);
    bebidaSelect.value = '';
    atualizarResumo();
});

document.addEventListener('DOMContentLoaded', () => {
    displayPizzas();
    loadCart();
});
