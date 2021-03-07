// Task 7 - Sum of Numbers

function sumOfNumbers(input) {
    // Read Input
    let numStr = input[0];

    // Logic
    let sum = 0;
    for (var i = 0; i < numStr.length; i++) {
        sum += Number(numStr[i]);
    }

    // Print
    console.log(`The sum of the digits is:${sum}`);
}

sumOfNumbers(['564891'])