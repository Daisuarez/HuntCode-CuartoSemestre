const modalContainer = document.getElementById('modal-container');
const modalOverlay = document.getElementById('modal-overlay'); // Cambiado de modal-everlay a modal-overlay
const cartBtn = document.getElementById('cart-btn');

const displayCart = () => {
    modalContainer.innerHTML ="";
    modalContainer.style.display = 'block';
    modalOverlay.style.display = 'block';
    // Modal Header
    const modalHeader = document.createElement('div');

    const modalClose = document.createElement('div');
    modalClose.innerText = "❌";
    modalClose.className = "modal-close";
    modalHeader.append(modalClose);

    /* con esto de aca abajo cierro y abro la pestañita*/
    modalClose.addEventListener('click', () =>{
        modalContainer.style.display = 'none';
        modalOverlay.style.display = 'none';
    })

    const modalTitle = document.createElement('div');
    modalTitle.innerText = "Cart";
    modalTitle.className = "modal-title";
    modalHeader.append(modalTitle);

    modalContainer.append(modalHeader);

    //modal Body
    cart.forEach((product) => {
        const modalBody = document.createElement('div');
        modalBody.className = "modal-body";
        modalBody.innerHTML = `
        <div class="product">
        <img class="product-img" src="${product.img}" />
        <div class="product-info">
        <h4>${product.productName}</h4>
        </div>
        <div class="quantity">
        <span class="quantity-btn-decrese">-</span>
        <span class="quantity-input">${product.quantity}</span>
        <span class ="quantity-btn-increase">+</span>
        </div>
            <div class="price">USD ${product.price * product.quantity}</div>
            <div class="delete-product">❌</div>
        </div>

        `;

        modalContainer.append(modalBody);

        
    });

    
        /* FOOTER, MODAL FOOTER MI REY AJAJ*/

        const modalFooter = document.createElement("div");
        modalFooter.className="modal-footer";
        modalFooter.innerHTML = `
            <div class="total-price">Total: </div>
        `;
        modalContainer.append(modalFooter);
};

cartBtn.addEventListener('click', displayCart);
