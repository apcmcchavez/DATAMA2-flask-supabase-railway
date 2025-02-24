function openForm(productName, productPrice) {
    document.getElementById("popupForm").style.display = "flex";
    document.getElementById("product-info").innerHTML = `Ordering: <b>${productName}</b> for <b>$${productPrice}</b>`;
    document.getElementById("product-name").value = productName;
}

function closeForm() {
    document.getElementById("popupForm").style.display = "none";
}

function showConfirmation(message) {
    const confirmationPopup = document.getElementById("confirmationPopup");
    document.getElementById("confirmationMessage").innerText = message;
    confirmationPopup.style.display = "flex";
}

function closeConfirmation() {
    document.getElementById("confirmationPopup").style.display = "none";
}

// Submit order to Flask backend
document.getElementById("orderForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const orderData = {
        name: document.getElementById("name").value,
        address: document.getElementById("address").value,
        payment: document.getElementById("payment").value,
        product: document.getElementById("product-name").value
    };

    fetch("/submit_order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(orderData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Order placed successfully!") {
            closeForm();
            showConfirmation("Your order has been placed successfully!");
        } else {
            showConfirmation("There was an error placing your order.");
        }
    })
    .catch(error => {
        showConfirmation("Error: Unable to submit your order.");
        console.error("Error:", error);
    });
});
