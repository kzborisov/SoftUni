// Task 5 - Training Lab
function area(input) {
    // Read Input Data
    let lengthMeters = Number(input[0]);
    let widthMeters = Number(input[1]);
    let widthCm;
    let lengthCm;
    let widthDesks;
    let lengthDesks;
    let result;

    // Calculations
    widthCm = (widthMeters * 100) - 100; // 100 for the coridor
    widthDesks = Math.floor(widthCm / 70);
    lengthCm = lengthMeters * 100;
    lengthDesks = Math.floor(lengthCm / 120);
    result = (widthDesks * lengthDesks) - 3; // for the door and the main desk

    // Print result formated to .00
    console.log(result.toFixed(0));
}

area(["8.4", "5.2"]);