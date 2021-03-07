// Task 9
function finalPrice(input) {
    let squareArea = Number(input[0]);
    let total = squareArea * 7.61;
    let discount = total * 0.18;
    let finalPrice = total - discount;
    console.log(`The final price is: ${finalPrice} lv.`);
    console.log(`The discount is: ${discount} lv.`)
}

finalPrice(["550"]);