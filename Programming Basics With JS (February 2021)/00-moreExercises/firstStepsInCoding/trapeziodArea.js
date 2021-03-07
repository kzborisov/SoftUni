// Task 1 - Trapeziod Area
function area(input) {
    // Read Input Data
    let sideA = Number(input[0]);
    let sideB = Number(input[1]);
    let height = Number(input[2]);

    // Calculations
    result = (sideA + sideB) * height / 2;

    // Print result formated to .00
    console.log(result.toFixed(2));
}

area(["8", "13", "7"]);