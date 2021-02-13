// Task 2 - Greater Number
function greaterNumber(input) {
    // Read Input Data
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);
    let result;

    // Calculations
    if (num1 > num2) {
        result = num1;
    } else {
        result = num2;
    }

    // Print result
    console.log(result);
}

greaterNumber(["-5", "5"]);