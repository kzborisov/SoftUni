// Task 2 - Add Bags

function addBags(input){
    // Read Input
    let above20Price = Number(input.shift());
    let bagsWeight = Number(input.shift());
    let daysLeft = Number(input.shift());
    let bagsCount = Number(input.shift());

    // Logic
    let price = 0;

    if (bagsWeight > 20){
        price = above20Price;
    } else if (bagsWeight >= 10) {
        price = above20Price * 0.5;  // 50% of the price for the bags heavier than 20kg
    } else if(bagsWeight < 10) {
        price = above20Price * 0.2;  // 20% of the price for the bags heavier than 20kg
    }

    if (daysLeft > 30) {
        price += price * 0.10;
    } else if (daysLeft >= 7) {
        price += price * 0.15;
    } else if (daysLeft < 7) {
        price += price * 0.40;
    }
    price *= bagsCount;

    // Print Result
    console.log(`The total price of bags is: ${price.toFixed(2)} lv. `);
}

addBags(["30",
"18",
"15",
"2"])