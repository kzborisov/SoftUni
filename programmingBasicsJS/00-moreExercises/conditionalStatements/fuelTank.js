// Task 8 - Fuel Tank

function fuelTank(input) {
    // Read Input Data
    let fuelType = input[0];
    let litters = Number(input[1]);

    // Calculations
    let fuels = ["Diesel", "Gasoline", "Gas"];

    // Check for inavlid fuel.
    if (!fuels.includes(fuelType)) {
        console.log("Invalid fuel!");
        return;
    }

    // Print result
    if (litters >= 25) {
        console.log(`You have enough ${fuelType.toLowerCase()}.`);
    } else if(litters < 25) {
        console.log(`Fill your tank with ${fuelType.toLowerCase()}!`)
    }
}

fuelTank(["Diesel", "10"]);