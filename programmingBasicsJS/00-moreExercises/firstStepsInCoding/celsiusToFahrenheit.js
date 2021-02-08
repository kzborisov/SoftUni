// Task 2 - Covert Celsius to Fahrenheit
function convertToFahrenheit(input) {
    // Read Input Data and initialize variables
    let celsius = Number(input[0]);
    let result;

    // Calculations
    // F = °C × 1,8 + 32.
    result = celsius * 1.8 + 32;

    // Print result formated to .00
    console.log(result.toFixed(2));
}

convertToFahrenheit(["-5.5"]);