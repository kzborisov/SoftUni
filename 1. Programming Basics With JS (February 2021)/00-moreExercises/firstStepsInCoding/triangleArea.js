// Task 2 - Triangle Area
function area(input) {
    // Read Input Data
    let side = Number(input[0]);
    let height = Number(input[1]);

    // Calculations
    result = (side * height) / 2;

    // Print result formated to .00
    console.log(result.toFixed(2));
}

area(["1.23456", "4.56789"]);