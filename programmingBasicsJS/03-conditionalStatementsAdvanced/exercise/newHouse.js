// Task 3 - New House

function newHouse(input) {
    // Read Input Data
    let flowerType = input[0];
    let flowerCount = Number(input[1]);
    let budget = Number(input[2]);

    // Logic
    let flowerPriceMap = {
        "Roses": 5,
        "Dahlias": 3.80,
        "Tulips": 2.80,
        "Narcissus": 3,
        "Gladiolus": 2.50
    };

    let price = flowerPriceMap[flowerType] * flowerCount;
;
    if (flowerType === "Roses" && flowerCount > 80) {
        price *= 0.90;
    } else if (flowerType === "Dahlias" && flowerCount > 90) {
        price *= 0.85;
    } else if (flowerType === "Tulips" && flowerCount > 80) {
        price *= 0.85;
    } else if (flowerType === "Narcissus" && flowerCount < 120) {
        price += price * 0.15;
    } else if (flowerType === "Gladiolus" && flowerCount < 80) {
        price += price * 0.20;
    }

    // Print Result
    if (price <= budget) {
        console.log(`Hey, you have a great garden with ${flowerCount} ${flowerType} and ${(budget - price).toFixed(2)} leva left.`)
    } else {
        console.log(`Not enough money, you need ${(price - budget).toFixed(2)} leva more.`);
    }
}

newHouse(["Narcissus",
"120",
"360"]);
