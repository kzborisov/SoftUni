// Task 6 - Charity Campaign
function calcTotalSum(input) {
    let days = Number(input[0]);
    let bakers = Number(input[1]);
    let cakes = Number(input[2]);
    let waffles = Number(input[3]);
    let pancakes = Number(input[4]);

    let sumPerDay = bakers * ((cakes * 45) + (waffles * 5.80) + (pancakes * 3.20));
    let totalSum = sumPerDay * days;
    let result = totalSum - (totalSum / 8);
    console.log(result);
}

calcTotalSum(["131", "5", "9", "33", "46"]);