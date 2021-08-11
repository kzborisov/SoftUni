// Task 6 - Pets

function pets(input) {
    // Read Input Data
    let days = Number(input[0]);
    let foodLeft = Number(input[1]);
    let dogFoodPerDay = Number(input[2]);
    let catFoodPerDay = Number(input[3]);
    let turtleFoodPerDay = Number(input[4]);  //In grams

    // Calculations
    // Convert turtle food to Kg
    let turtleFoodKg = turtleFoodPerDay / 1000;
    let totalFood = days * (dogFoodPerDay + catFoodPerDay + turtleFoodKg);

    // Print result
    if (totalFood <= foodLeft) {
        let leftover = Math.floor(foodLeft - totalFood);
        console.log(`${leftover} kilos of food left.`)
    } else {
        let foodNeeded = Math.ceil(totalFood - foodLeft);
        console.log(`${foodNeeded} more kilos of food are needed.`);
    }
}

pets(["5", "10", "2.1", "0.8", "321"]);