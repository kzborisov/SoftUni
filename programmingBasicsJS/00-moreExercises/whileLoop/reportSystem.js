// Task 2 - Report System

function reportSystem(input) {
    // Read Input
    let expectedSum = Number(input.shift());

    // Logic
    let totalSum = 0;
    let counter = 0;

    let paymentType = {
        "cash": 0,
        "cashPayments": 0,
        "card": 0,
        "cardPayments": 0
    };

    while (true) {
        let itemsPrice = input.shift();

        if (itemsPrice === "End" || totalSum >= expectedSum){
            break;
        }

        if (counter % 2 === 0){
            // Cash only
            if (Number(itemsPrice) > 100){
                console.log("Error in transaction!");
            } else {
                totalSum += Number(itemsPrice);
                paymentType["cash"] += Number(itemsPrice);
                paymentType["cashPayments"]++;
                console.log("Product sold!");
            }
        } else {
            // Card only
            if (Number(itemsPrice) < 10){
                console.log("Error in transaction!");
            } else {
                totalSum += Number(itemsPrice);
                paymentType["card"] += Number(itemsPrice);
                paymentType["cardPayments"]++;
                console.log("Product sold!");
            }
        }
        counter++;
    }

    // Print Result
    if (totalSum < expectedSum){
        console.log("Failed to collect required money for charity.");
    } else {
        console.log(`Average CS: ${(paymentType["cash"] / paymentType["cashPayments"]).toFixed(2)}`);
        console.log(`Average CC: ${(paymentType["card"] / paymentType["cardPayments"]).toFixed(2)}`);
    }
}

reportSystem([
    "500",
    "120",
    "8",
    "63",
    "256",
    "78",
    "317",
    "End"]);