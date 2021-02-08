// Task 9 - Weather Forecast
function forecast(input) {
    // Read Input Data
    let weather = input[0]; // string

    // Print result
    if (weather == 'sunny') {
        console.log("It's warm outside!");
    }
    else {
        console.log("It's cold outside!");
    }
}

forecast(["cloudy"]);