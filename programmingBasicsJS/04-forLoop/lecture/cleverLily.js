// Task 9 - Clever Lily

function cleverLily(input) {
    // Read Input
    let age = Number(input[0]);
    let washingMachinePrice = Number(input[1]);
    let toyPrice = Number(input[2]);

    // Logic
    let money = 0;
    let moreMoney = 10;
    let toysCount = 0;

    for (let i = 1; i <= age; i++) {
        if (i % 2 == 0) {
            money += moreMoney - 1;
            moreMoney += 10;
        } else {
            toysCount += 1;
        }
    }

    let totalMoney = (toyPrice * toysCount) + money;

    // Print Result
    if (totalMoney >= washingMachinePrice) {
        console.log(`Yes! ${(totalMoney - washingMachinePrice).toFixed(2)}`);
    } else {
        console.log(`No! ${(washingMachinePrice - totalMoney).toFixed(2)}`);
    }
}

cleverLily(["21", "1570.98", "3"]);