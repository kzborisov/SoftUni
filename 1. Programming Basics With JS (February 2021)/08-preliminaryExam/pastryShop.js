function pastryShop(input) {
    // Read Input
    let cakeType = input.shift();
    let cakesCount = Number(input.shift());
    let day = Number(input.shift());

    // Logic
    let beforeOrAfter = "before";

    let priceMap = {
        "before": {
            "Cake": 24,
            "Souffle": 6.66,
            "Baklava": 12.60
        },
        "after": {
            "Cake": 28.70,
            "Souffle": 9.80,
            "Baklava": 16.98
        },
    };

    if (day > 15){
        beforeOrAfter = "after";
    }

    let price = priceMap[beforeOrAfter][cakeType] * cakesCount;

    if (day <= 15){
        price *= 0.90;
    } 
    if (day <= 22){
        if (price > 200){
            price *= 0.75;
        } else if (price >= 100) {
            price *= 0.85
        }
    }

    // Print result
    console.log(price.toFixed(2));
}

pastryShop(["Souffle", "20", "24"]);