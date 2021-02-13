// Task 5 - Guess the Password
function guessPassword(input) {
    // Read Input Data
    let password = input[0];
    let result;

    // Calculations
    if (password === 's3cr3t!P@ssw0rd') {
        result = 'Welcome';
    } else {
        result = 'Wrong password!';
    }

    // Print result
    console.log(result);
}

guessPassword(["s3cr3t!P@ssw0rd"]);