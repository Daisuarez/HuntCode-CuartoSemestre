const shopContent = document.getElementById("shopContent");
const cart = []; /* Nuestro carrito, array vacio*/ 
/* ACA CREAMOS LOS DIV QUE CONTENDRAN LOS ITEM COMO IMG*/
productos.forEach((product) =>{
    const content = document.createElement("div");
    content.classList.add("productContentDiv"); // esto para agregarle una clase al div que nos genera js asi lo trabajamos desde css
    content.innerHTML = `
    <img src="${product.img}"> 
    <h3>${product.productName}</h3>
    <p>USD ${product.price}</p>
    `;
    shopContent.append(content);
    
 /* con lo de aca abajo va creando el boton de la card */
    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar";
    content.append(buyButton); 



    buyButton.addEventListener("click", ()=>{
        cart.push({
            id: product.id,
            productName: product.productName,
            price: product.price,
            quantity:product.quantity,
            img: product.img,
        })
        console.log(cart);
    })

});

