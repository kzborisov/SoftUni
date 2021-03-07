// Task 6 - Fishland
function calcNeededMoney(input) {
    // Read Input Data
    let mackerelPrice = Number(input[0]);
    let toyPrice = Number(input[1]);
    let bonitoWeight = Number(input[2]);
    let horseMackerelWeight = Number(input[3]);
    let oysterWeight = Number(input[4]);

    // Initialize variables
    let totalBonitoPrice;
    let totalHorseMackerelPrice;
    let totalOysterPrice;
    let result;

    // Calculations
    totalBonitoPrice = (mackerelPrice + mackerelPrice * 0.60) * bonitoWeight;
    totalHorseMackerelPrice = (toyPrice + toyPrice * 0.80) * horseMackerelWeight;
    totalOysterPrice = oysterWeight * 7.50;
    result = totalBonitoPrice + totalHorseMackerelPrice + totalOysterPrice;

    // Print result formated to .00
    console.log(result.toFixed(2));
}

calcNeededMoney(["5.55", "3.57", "4.3", "3.6", "7"]);