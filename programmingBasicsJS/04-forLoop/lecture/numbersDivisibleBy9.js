// Task 8 - Numbers Divisible by 9

function numbersDivisibleBy9(input) {
    // Read Input
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);

    // Logic
    let sum = 0;
    let nums = [];
    for (var i = num1; i <= num2; i++) {
        if (i % 9 === 0) {
            sum += i;
            nums.push(i);
        }
    }

    // Print Result
    console.log(`The sum: ${sum}`);
    for (var i = 0; i < nums.length; i++) {
        console.log(nums[i]);
    }
}

numbersDivisibleBy9(['100', "200"])