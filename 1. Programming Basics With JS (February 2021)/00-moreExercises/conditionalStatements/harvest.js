// Task 3 - Harvest

function harvest(input) {
    // Read Input Data
    let grapeSqM = Number(input[0]);
    let grapePerSqrM = Number(input[1]);
    let neededWine = Number(input[2]);
    let workersCount = Number(input[3]);

    // Calculations
    let totalGrape = grapeSqM * grapePerSqrM;
    let wine = 0.4 * totalGrape / 2.5;

    // Print result
    if (wine < neededWine){
        let result = Math.floor(neededWine - wine);
        console.log(`It will be a tough winter! More ${result} liters wine needed.`);
    } else if (wine >= neededWine){
        let result = Math.ceil(wine - neededWine);
        console.log(`Good harvest this year! Total wine: ${Math.floor(wine)} liters.`);
        console.log(`${result} liters left -> ${Math.ceil(result / workersCount)} liters per person.`)
    }
}

harvest(["1020", "1.5", "425", "4"]);