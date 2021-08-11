// Task 3 - Deposit Calculator
function depositCalculator(input) {
    let deposit = Number(input[0]);
    let timeFrame = Number(input[1]);
    let anualInterestRate = Number(input[2]);
    let interest = (deposit * anualInterestRate) / 100;
    let result = deposit + timeFrame * (interest / 12);
    console.log(result);
}

depositCalculator(["2350", "6", "7"])