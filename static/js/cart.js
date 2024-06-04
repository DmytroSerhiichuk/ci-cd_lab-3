console.log("Hello world")

var updateBtns = document.getElementsByClassName('update-cart');


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function (event) {
        event.preventDefault();
        console.log("Hello world" + i)

        var productId = this.dataset.product;
        var action = this.dataset.action;
        var quantityInput = document.getElementById('quantity');
        var quantity = quantityInput ? parseInt(quantityInput.value, 10) : 1;

        console.log('productId:', productId, 'Action:', action, 'Quantity:', quantity);

        console.log('USER:', user);
        if (user == 'AnonymousUser') {
            console.log("User can't log in");
        } else {
            updateUserOrder(productId, action, quantity);
        }
    });
}

function updateUserOrder(productId, action, quantity) {
    console.log('User is logged in, sending data...');

    var url = '/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action, 'quantity': quantity })
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log("Yep")
        console.log('data', data);
        location.reload();
    });
}