// Task 4 - Personal Titles

function personalTitles(input) {
    // Read Input Data
    let age = Number(input[0]);
    let gender = input[1];

    // Calculations
    if (gender === 'm') {
        if (age >= 16) {
            console.log("Mr.");
        } else {
            console.log("Master");
        }
    } else {
        if (age >= 16) {
            console.log("Ms.");
        } else {
            console.log("Miss")
        }
    }
}

personalTitles((["17", "m"]));