// Task 4 - Fishing Boat

function fishingBoat(input) {
    // Read Input Data
    let budget = Number(input[0]);
    let season = input[1];
    let fishermenCount = Number(input[2]);

    // Logic
    let priceMap = {
        "Spring": 3000,
        "Summer": 4200,
        "Autumn": 4200,
        "Winter": 2600
    };

    let price = priceMap[season]
    if (fishermenCount <= 6) {
        price *= 0.90;
    } else if (fishermenCount > 6 && fishermenCount <= 11) {
        price *= 0.85;
    } else if (fishermenCount > 11) {
        price *= 0.75;
    }

    if (!(season === "Autumn") && fishermenCount % 2 === 0) {
        price *= 0.95;
    }

    // Print Result
    if (price <= budget) {
        console.log(`Yes! You have ${(budget-price).toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${(price - budget).toFixed(2)} leva.`);
    }
}

fishingBoat(["2000",
"Winter",
"13"]);