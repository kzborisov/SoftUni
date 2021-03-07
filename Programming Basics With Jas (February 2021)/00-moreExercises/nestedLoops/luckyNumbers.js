// Task 3 - Lucky Numbers

function luckyNumbers(input) {
    // Read Input
    let num = Number(input.shift());

    // Logic
    for (let first = 1; first < 10; first++) {
        for(let second = 1; second < 10; second++) {
            for(let third = 1; third < 10; third++) {
                for(let fourth = 1; fourth < 10; fourth++) {
                    let isEqualSum = (first + second) === (third + fourth);
                    let isDivisible = num % (first + second) === 0;
                    if (isEqualSum && isDivisible) {
                        process.stdout.write(`${first}${second}${third}${fourth} `);
                    }
                }
            }
        }
    }
}

luckyNumbers(["3"]);