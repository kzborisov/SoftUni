// Task 4 - Sequence 2k + 1

function sumNumbers(input) {
    // Read Input
    let first = Number(input.shift());

    // Logic
    let counter = 1;

    while (counter <= first) {
        console.log(counter);
        counter = counter * 2 + 1;
    }
}

sumNumbers(["3"]);