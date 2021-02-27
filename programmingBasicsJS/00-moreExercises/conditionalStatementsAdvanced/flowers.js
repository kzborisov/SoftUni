// Task 3 - Flowers

function flowers(input) {
    // Read Input Data
    let chrysanthemumsCount = Number(input[0]);
    let rosesCount = Number(input[1]);
    let tulipsCount = Number(input[2]);
    let season = input[3];
    let holiday = input[4];

    // Logic
    let flowersPriceMap = {
        'Spring':{
            'chrysanthemums': 2.00,
            'roses': 4.10,
            'tulips': 2.50
        },
        'Summer': {
            'chrysanthemums': 2.00,
            'roses': 4.10,
            'tulips': 2.50
        },
        'Autumn': {
            'chrysanthemums': 3.75,
            'roses': 4.50,
            'tulips': 4.15
        },
        'Winter': {
            'chrysanthemums': 3.75,
            'roses': 4.50,
            'tulips': 4.15
        },
    };
    var total = 0;

    for (var property in flowersPriceMap[season]) {
        total += flowersPriceMap[season][property];
    }

    let flowersPrice = 
    flowersPriceMap[season]['chrysanthemums'] * chrysanthemumsCount +
    flowersPriceMap[season]['roses'] * rosesCount +
    flowersPriceMap[season]['tulips'] * tulipsCount;
    
    if (holiday === 'Y') {
        flowersPrice += flowersPrice * 0.15;
    };

    if (tulipsCount > 7 && season === "Spring") {
        flowersPrice *= 0.95;  // 5% Discount
    } else if (rosesCount >= 10 && season === "Winter") {
        flowersPrice *= 0.90;  // !0% Discount
    };

    if ((chrysanthemumsCount + rosesCount + tulipsCount) > 20) {
        flowersPrice *= 0.80;  // 20% Discount
    };

    flowersPrice += 2;  // Price to arrange to flowers

    // Print Result
    console.log(flowersPrice.toFixed(2));
}

flowers(["10",
"10",
"10",
"Autumn",
"N"]);
