function solve() {
    [...document.querySelectorAll(".product")].forEach((el) =>
        el.addEventListener("click", onClick)
    );
    document.querySelector(".checkout").addEventListener("click", onCheckout);

    const textArea = document.querySelector("textarea");

    let total = 0;
    const products = [];

    function onCheckout(e) {
        textArea.value += `You bought ${products.join(
            ", "
        )} for ${total.toFixed(2)}.`;
        [...document.querySelectorAll("button")].forEach(
            (btn) => (btn.disabled = true)
        );
    }

    function onClick(e) {
        if (e.target.tagName === "BUTTON") {
            const productName =
                e.currentTarget.querySelector(".product-title").textContent;
            const money = Number(
                e.currentTarget.querySelector(".product-line-price").textContent
            );

            if (!products.includes(productName)) {
                products.push(productName);
            }
            total += money;
            textArea.value += `Added ${productName} for ${money.toFixed(
                2
            )} to the cart.\n`;
        }
    }
}
