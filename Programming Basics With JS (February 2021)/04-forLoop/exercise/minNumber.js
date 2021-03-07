// Task 9 - Min Number

function minNumber(input) {
    // Read Input
    let numbersCount = Number(input[0]);

    // Logic
    let numArr = [];
    for (let i = 1; i <= numbersCount; i++) {
        let number = Number(input[i]);
        numArr.push(number);
    }

    // Print Result
    console.log(Math.min(...numArr));
}

minNumber(["4",
"45",
"-20",
"7",
"99"]);