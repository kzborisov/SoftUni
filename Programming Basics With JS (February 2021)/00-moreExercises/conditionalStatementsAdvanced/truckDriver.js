// Task 6 - Truck Driver

function truckDriver(input) {
    // Read Input Data
    let season = input[0];
    let kilometers = Number(input[1]);

    // Logic
    let money = 0;
    if (kilometers <= 5000) {
        if (season === 'Spring' || season === 'Autumn') {
            money = kilometers * 0.75;
        } else if (season === 'Summer') {
            money = kilometers * 0.90;
        } else {
            money = kilometers * 1.05;
        }
    } else if (kilometers > 5000 && kilometers <= 10000) {
        if (season === 'Spring' || season === 'Autumn') {
            money = kilometers * 0.95;
        } else if (season === 'Summer') {
            money = kilometers * 1.10;
        } else {
            money = kilometers * 1.25;
        }
    } else if (kilometers > 10000 && kilometers <= 20000) {
        money = kilometers * 1.45;
    }

    money *= 0.90 * 4;


    // Print Result
    console.log(money.toFixed(2));
}

truckDriver(["Winter", "16042"])