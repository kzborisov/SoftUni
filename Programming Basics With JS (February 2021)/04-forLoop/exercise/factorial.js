// Task 4 - Factorial

function factorial(input) {
    // Read Input
    let num = Number(input[0]);

    // Logic
    let result = 1;
    for (let i = 1; i <= num; i++) {
        result *= i;
    }

    // Print result
    console.log(result);
}

factorial(["4"]);