const shopContent = document.getElementById("shopContent");
const cart = []; /* Nuestro carrito, array vacío */ 

productos.forEach((product) => {
    const content = document.createElement("div");
    content.classList.add("productContentDiv");
    content.innerHTML = `
    <img src="${product.img}"> 
    <h3>${product.productName}</h3>
    <p>USD ${product.price}</p>
    `;
    shopContent.append(content);

    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar";
    content.append(buyButton);

    buyButton.addEventListener("click", () => {
        const repeatIndex = cart.findIndex((repeatProduct) => repeatProduct.id === product.id);
        if (repeatIndex !== -1) {
            cart[repeatIndex].quantity++;
            displayCartCounter()
        } else {
            cart.push({
                id: product.id,
                productName: product.productName,
                price: product.price,
                quantity: 1, // Inicializa la cantidad en 1 cuando se agrega un nuevo producto
                img: product.img,
            });
            displayCartCounter()
        }
        console.log(cart);
    });
});
