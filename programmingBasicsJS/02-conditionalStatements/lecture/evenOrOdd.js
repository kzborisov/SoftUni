// Task 3 - Even or Odd
function evenOrOdd(input) {
    // Read Input Data
    let num1 = Number(input[0]);
    let result;

    // Calculations
    if (num1 % 2 == 0) {
        result = 'even';
    } else {
        result = 'odd';
    }

    // Print result
    console.log(result);
}

evenOrOdd(["1024"]);