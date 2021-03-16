// Task 8 - Food For Pets 

function foodForPets(input) {
    // Read Input
    let days = Number(input.shift());
    let totalFood = Number(input.shift());

    // Logic
    let totalDogEatenFood = 0;
    let totalCatEatenFood = 0;
    let biscuits = 0;

    for (let day = 1; day <= days; day++){
        let dogFoodPerDay = Number(input.shift());
        totalDogEatenFood += dogFoodPerDay;

        let catFoodPerDay = Number(input.shift());
        totalCatEatenFood += catFoodPerDay;

        if (day % 3 === 0){
            biscuits += (dogFoodPerDay + catFoodPerDay) * 0.1;
        }
    }

    let total = totalDogEatenFood + totalCatEatenFood;

    // Print Result
    console.log(`Total eaten biscuits: ${Math.round(biscuits)}gr.`);
    console.log(`${((total / totalFood) * 100).toFixed(2)}% of the food has been eaten.`);
    console.log(`${((totalDogEatenFood / total)* 100).toFixed(2)}% eaten from the dog.`);
    console.log(`${((totalCatEatenFood/ total) * 100).toFixed(2)}% eaten from the cat.`);
}

foodForPets(["3",
"500",
"100",
"30",
"110",
"25",
"120",
"35"])
;