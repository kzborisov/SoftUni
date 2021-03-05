// Task 1 - Dishwasher

function dishwasher(input) {
    // Read Input
    let bottlesCount = Number(input.shift());

    // Logic
    let detergent = bottlesCount * 750; // 750ml/bottle
    let counter = 0;
    let washedDishes = {
        'dishes': 0,
        'pots': 0,
    };

    while (true) {
        let dishesCount = input.shift();
        counter ++;

        if (dishesCount === "End" || detergent < 0){
            break;
        } else {
            // Every third time the dishes are pots - 15 ml per pot.
            if (counter % 3 === 0){
                detergent -= Number(dishesCount) * 15;
                washedDishes['pots'] += Number(dishesCount);
            } else {
                detergent -= dishesCount * 5;
                washedDishes['dishes'] += Number(dishesCount);
            }
        }
    }

    // Print Result
    if (detergent >= 0){
        console.log("Detergent was enough!");
        console.log(`${washedDishes["dishes"]} dishes and ${washedDishes["pots"]} pots were washed.`);
        console.log(`Leftover detergent ${detergent} ml.`);
    } else {
        console.log(`Not enough detergent, ${Math.abs(detergent)} ml. more necessary!`)
    }
}

dishwasher([
    "2",
    "53",
    "65",
    "55",
    "End"]);

dishwasher(["1",
"10",
"15",
"10",
"12",
"13",
"30",]);
