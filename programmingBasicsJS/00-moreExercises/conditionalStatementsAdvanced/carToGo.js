// Task 4 - Car To Go

function carToGo(input) {
    // Read Input Data
    let budget = Number(input[0]);
    let season = input[1];

    // Logic
    let carMap = {
        'Summer' : 'Cabrio',
        'Winter' : 'Jeep'
    };

    let sum = 0;
    let car = carMap[season];
    let classType = 'Economy class';

    if (budget > 500) {
        classType = 'Luxury class';
        car = 'Jeep';
        sum = budget * 0.90;
    } else if (budget > 100 && budget <= 500) {
        classType = 'Compact class';
        if (season === "Summer") {
            sum = budget * 0.45;
        } else if (season === "Winter") {
            sum = budget * 0.80;
        }
    } else if (budget <= 100) {
        classType = 'Economy class';
        if (season === "Summer") {
            sum = budget * 0.35;
        } else if (season === "Winter") {
            sum = budget * 0.65;
        }
    }


    // Print Result
    console.log(classType);
    console.log(`${car} - ${sum.toFixed(2)}`);
}

carToGo(["70.50", "Winter"])