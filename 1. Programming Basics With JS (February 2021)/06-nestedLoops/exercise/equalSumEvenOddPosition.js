// Task 2 - Equal Sum Even Odd Position

function equalSum(input) {
    // Read Input
    let start = Number(input.shift());
    let end = Number(input.shift());

    // Logic
    for (let i = start; i <= end; i++) {
        let evenSum = 0;
        let oddSum = 0;
        let num = String(i);

        for (let j = 0; j < num.length; j++) {
            let current = Number(num[j]);
            if (j % 2 == 0) {
                evenSum += current;
            } else {
                oddSum += current;
            }
        }
        if (evenSum == oddSum) {
            process.stdout.write(`${i} `);
        }
    }
}

equalSum(["100000",
"100050"]);