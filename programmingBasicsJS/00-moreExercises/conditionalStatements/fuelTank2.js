// Task 9 - Fuel Tank 2

function fuelTank2(input) {
    // Read Input Data
    let fuelType = input[0];
    let litters = Number(input[1]);
    let clubCard = input[2];

    // Calculations
    let fuelMap = {
        'Gasoline': 2.22,
        'Diesel': 2.33,
        'Gas': 0.93,
        'GasolineWithDiscount': 2.22 - 0.18,
        'DieselWithDiscount': 2.33 - 0.12,
        'GasWithDiscount': 0.93 - 0.08,
    };

    let result;
    // Print result
    if (clubCard.toLowerCase() === "yes"){
        result = fuelMap[fuelType+'WithDiscount'] * litters;
    } else {
        result = fuelMap[fuelType] * litters;
    }

    if (litters > 25){
        result *= 0.90;
    } else if (litters > 20) {
        result *= 0.92
    }
    console.log(`${result.toFixed(2)} lv.`);
}

fuelTank2(["Diesel", "19", "No"]);