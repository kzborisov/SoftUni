// Task 9 - Weather Forecast
function forecast(input) {
    // Read Input Data
    let degrees = Number(input[0]);

    // Print result
    if (degrees >= 26.00 && degrees <= 35.9) {
        console.log("Hot");
    }
    else if (degrees >= 20.01 && degrees <= 25.9) {
        console.log("Warm");
    }
    else if (degrees >= 15.00 && degrees <= 20.00) {
        console.log("Mild");
    }
    else if (degrees >= 12.00 && degrees <= 14.9) {
        console.log("Cool");
    }
    else if (degrees >= 5.00 && degrees <= 11.9) {
        console.log("Cold");
    }
    else {
        console.log("unknown");
    }
}

forecast(["0"]);