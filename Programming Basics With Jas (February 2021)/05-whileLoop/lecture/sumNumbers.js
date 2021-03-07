// Task 3 - Sum Numbers

function sumNumbers(input) {
    // Read Input
    let first = Number(input.shift());
    let next = Number(input.shift());

    // Logic
    while (next < first) {
        next += Number(input.shift());
    }
    console.log(next);
}

sumNumbers(["20",
"1",
"2",
"3",
"4",
"5",
"6"]);