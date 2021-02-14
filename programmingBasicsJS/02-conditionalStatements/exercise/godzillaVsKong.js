// Task 6 - Godzilla vs. Kong

function calcBudget(input) {
    // Read Input Data
    let budget = Number(input[0]);
    let statistCount = Number(input[1]);
    let clothingPricePerStatist = Number(input[2]);

    let decorPrice;
    let clothingPrice;
    let totalSum;

    // Calculations
    decorPrice = budget * .10;
    clothingPrice = statistCount * clothingPricePerStatist;

    if (statistCount > 150) {
        clothingPrice = clothingPrice * 0.90;
    }

    totalSum = decorPrice + clothingPrice;

    // Print result
    if (totalSum <= budget) {
        console.log("Action!");
        console.log(`Wingard starts filming with ${(budget - totalSum).toFixed(2)} leva left.`);
    } else {
        console.log("Not enough money!");
        console.log(`Wingard needs ${Math.abs(totalSum - budget).toFixed(2)} leva more.`)
    }
}

calcBudget(["15437.62",
"186",
"57.99"]);