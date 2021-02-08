// Task 8 - Circle Area And Perimeter
function calcNeededMoney(input) {
    // Read Input Data
    let radius = Number(input[0]);

    // Initialize variables
    let perimeter;
    let area;

    // Calculations
    area = Math.PI * Math.pow(radius, 2);
    perimeter = 2 * Math.PI * radius;

    // Print result formated to .00
    console.log(area.toFixed(2));
    console.log(perimeter.toFixed(2));
}

calcNeededMoney(["4.5"]);