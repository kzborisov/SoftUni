// Task 10 - Invalid Number

function invalidNumber(input) {
    // Read Input Data
    let num = Number(input[0]);

    // Calculations
    if (num >= 100 && num <= 200 || num === 0){
        return;
    } else {
        console.log("invalid");
    }
}

invalidNumber((["200"]));
