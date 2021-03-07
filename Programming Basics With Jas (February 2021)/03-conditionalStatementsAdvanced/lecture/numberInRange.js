// Task 6 - Number in Range

function numberInRange(input) {
    // Read Input Data
    let num = Number(input[0]);

    // Calculations
    if (num >= -100 && num <= 100) {
        if (num === 0) {
            console.log("No")
        }
        else {
            console.log("Yes")
        }
    } else {
        console.log("No")
    }
}

numberInRange((["100"]));