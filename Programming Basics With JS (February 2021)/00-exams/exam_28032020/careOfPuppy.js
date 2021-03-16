// Task 10 - Care Of Puppy 

function careOfPuppy(input) {
    // Read Input
    let totalFood = Number(input.shift());
    let foodEaten = input.shift();

    // Logic
    let foodInGr = totalFood * 1000;
    let totalEatenFood = 0
    while (foodEaten !== "Adopted"){
        let currentFood = Number(foodEaten);
        totalEatenFood += currentFood;
        foodEaten = input.shift();
    }

    // Print Result
    if (totalEatenFood <= foodInGr){
        console.log(`Food is enough! Leftovers: ${Math.abs(totalEatenFood - foodInGr)} grams.`);
    } else {
        console.log(`Food is not enough. You need ${Math.abs(foodInGr - totalEatenFood)} grams more.`);
    }
}

careOfPuppy(["2",
"999",
"456",
"999",
"999",
"123",
"456",
"Adopted"])
;