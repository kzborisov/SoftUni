// Task 7 - Toy Store

function toyStore(input) {
    // Read Input Data
    let tripPrice = Number(input[0]);
    let puzzleCount = Number(input[1]);
    let dollsCount = Number(input[2]);
    let teddyBearsCount = Number(input[3]);
    let minionsCount = Number(input[4]);
    let truckCount = Number(input[5]);

    let totalPrice;
    let toysTotalCount;

    // Calculations
    totalPrice = (puzzleCount * 2.60) + (dollsCount * 3) + (teddyBearsCount * 4.10) + (minionsCount * 8.20) + (truckCount * 2);
    toysTotalCount = puzzleCount + dollsCount + teddyBearsCount + minionsCount + truckCount;

    if (toysTotalCount >= 50) {
        // 25% Discount
        totalPrice = totalPrice - (totalPrice * 0.25);
    }

    // 10% of the Total Price is rent
    totalPrice = totalPrice * 0.90;

    // Print result formated to .00
    // Check if Petya has enough money for the trip
    if (totalPrice >= tripPrice) {
        let moneyLeft = totalPrice - tripPrice;
        console.log(`Yes! ${moneyLeft.toFixed(2)} lv left.`);
    } else {
        let neededMoney = Math.abs(tripPrice - totalPrice);
        console.log(`Not enough money! ${neededMoney.toFixed(2)} lv needed.`)
    }
}

toyStore(["320", "8", "2", "5", "5", "1"])