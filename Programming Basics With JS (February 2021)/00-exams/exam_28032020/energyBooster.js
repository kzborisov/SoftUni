// Task 5 - Energy Booster 

function energyBooster(input) {
    // Read Input
    let fruit = input.shift();
    let size = input.shift();  // Big or small
    let count = Number(input.shift());  // In seconds

    // Logic
    let priceMap = {
        "small": {
            "Watermelon": 56*2,
            "Mango": 36.66*2,
            "Pineapple": 42.10*2,
            "Raspberry": 20*2
        },
        "big": {
            "Watermelon": 28.70*5,
            "Mango": 19.60*5,
            "Pineapple": 24.80*5,
            "Raspberry": 15.20*5
        }
    };

    let totalPrice = priceMap[size][fruit] * count;

    if (totalPrice > 1000){
        totalPrice *= 0.50;
    } else if (totalPrice >= 400){
        totalPrice *= 0.85;
    }

    // Print Result
    console.log(`${totalPrice.toFixed(2)} lv.`);
}

energyBooster(["Watermelon",
"big",
"4"])
;