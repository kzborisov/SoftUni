// Task 5 - Vacation

function vacation(input) {
    // Read Input Data
    let budget = Number(input[0]);
    let season = input[1];

    // Logic
    let placeMap = {
        'Summer': 'Alaska',
        'Winter': 'Morocco'
    };

    let placeToStay = 'Hotel';
    let location = placeMap[season];;
    let sum = 0;

    if (budget > 3000) {
        placeToStay = 'Hotel';
        sum = budget * 0.90;
    } else if (budget > 1000 && budget <= 3000) {
        placeToStay = 'Hut';
        if (season === 'Summer') {
            sum = budget * 0.80;
        } else if (season === 'Winter') {
            sum = budget * 0.60;
        }
    } else {
        placeToStay = 'Camp';
        if (season === 'Summer') {
            sum = budget * 0.65;
        } else if (season === 'Winter') {
            sum = budget * 0.45;
        }
    }

    // Print Result
    console.log(`${location} - ${placeToStay} - ${sum.toFixed(2)}`)
}

vacation(["3460", "Summer"])