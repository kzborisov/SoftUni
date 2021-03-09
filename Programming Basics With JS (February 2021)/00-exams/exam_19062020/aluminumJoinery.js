// Task 3 - Aluminun Joinery

function aluminumJoinery(input) {
    // Read Input Data
    let above20 = Number(input.shift());
    let bagsWeight = Number(input.shift());
    let days = Number(input.shift());
    let bagsCount = Number(input.shift());

    // Logic
    let totalPrice = 0;
    if (bagsWeight > 20){
        totalPrice  = above20;
    } else if (bagsWeight >= 10){
        totalPrice = above20 * 0.5;  // 50% of the price above 20 kilograms
    } else {
        totalPrice = above20 * 0.2;  // 20% of the price above 20 kilograms
    }

    if (days > 30) {
        totalPrice += totalPrice * 0.10;
    } else if (days >= 7){
        totalPrice += totalPrice * 0.15;
    } else {
        totalPrice += totalPrice * 0.40;
    }

    totalPrice *= bagsCount;

    // Print Result
    console.log(`The total price of bags is: ${totalPrice.toFixed(2)} lv. `);
}

agencyProfit([
"30",
"18",
"15",
"2"]); 