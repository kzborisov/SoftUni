// Task 4 - Vegetable Market
function calcIncome(input) {
    // Read Input Data and initialize variables
    let veggiesPrice = Number(input[0]);
    let fruitPrice = Number(input[1]);
    let veggiesWeight = Number(input[2]);
    let fruitWeight = Number(input[3]);

    let veggiesTotalPrice;
    let fruitTotalPrice;
    let result;

    // Calculations
    veggiesTotalPrice = veggiesWeight * veggiesPrice;
    fruitTotalPrice = fruitWeight * fruitPrice;
    // Convert to EURO if: 1 EURO = 1.94 BGN;
    result = (veggiesTotalPrice + fruitTotalPrice) / 1.94;

    // Print result formated to .00
    console.log(result.toFixed(2));
}

calcIncome(["1.5", "2.5", "10", "10"]);