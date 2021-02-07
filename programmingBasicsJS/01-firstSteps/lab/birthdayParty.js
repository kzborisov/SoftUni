// Task 5 - Birthday Party
function calcBudget(input) {
    let hallRent = Number(input[0]);
    let cakePrice = hallRent * 0.2;
    let drinksPrice = cakePrice - (cakePrice * 0.45);
    let animatorPrice = hallRent / 3;
    let result = hallRent + cakePrice + drinksPrice + animatorPrice;
    console.log(result);
}

calcBudget(["3720"]);