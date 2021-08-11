// Task 1 - Agency Profit

function agencyProfit(input) {
    // Read Input Data
    let name = input.shift();
    let adultTicketsCount = Number(input.shift());
    let childrenTicketsCount = Number(input.shift());
    let adultPrice = Number(input.shift());
    let servicePrice = Number(input.shift());

    // Logic
    let childrenPrice = adultPrice * 0.30 + servicePrice;  // adult ticket price - 70% + Service Price
    let totalPrice = (childrenTicketsCount * childrenPrice) + ((adultPrice + servicePrice) * adultTicketsCount);

    // Print Result
    console.log(`The profit of your agency from ${name} tickets is ${(totalPrice * 0.2).toFixed(2)} lv.`);
}

agencyProfit(["WizzAir", "15", "5", "120", "40"]); 