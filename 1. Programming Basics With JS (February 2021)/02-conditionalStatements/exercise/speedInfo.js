// Task 3 - Speed Info

function speedInfo(input) {
    // Read Input Data
    let speed = Number(input[0]);
    let result;


    // Calculations
    if (speed <= 10) {
        result = 'slow';
    } else if (speed <= 50) {
        result = 'average';
    } else if (speed <= 150) {
        result = 'fast';
    } else if (speed <= 1000) {
        result = 'ultra fast';
    } else {
        result = 'extremely fast';
    }

    // Print result - with a leading 0.
    console.log(result);
}

speedInfo(["3500"]);