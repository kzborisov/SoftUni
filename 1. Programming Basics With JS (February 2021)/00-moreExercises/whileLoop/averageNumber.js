// Task 5 - Average Number

function averageNumber(input) {
    // Read Input
    let num = Number(input.shift());

    // Logic
    let n = 0;
    let sum = 0;
    while (n < num) {
        let nextNum = Number(input.shift());
        sum += nextNum;
        n++;
    }

    // Print Result
    console.log((sum/n).toFixed(2));
}

averageNumber(["4",
"3",
"2",
"4",
"2"]);