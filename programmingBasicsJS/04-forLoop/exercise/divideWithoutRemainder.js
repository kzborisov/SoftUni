// Task 7 - Divide without remainder

function divideWithoutRemainder(input) {
    // Read Input
    let numbersCount = Number(input[0]);

    // Logic
    let counts = {
        'p1': 0,
        'p2': 0,
        'p3': 0
    };

    for (let i = 1; i <= numbersCount; i++) {
        let num = Number(input[i]);

        if (num % 2 === 0) {
            counts['p1']++;
        }
        if (num % 3 === 0) {
            counts['p2']++;
        }
        if (num % 4 === 0) {
            counts['p3']++;
        }
    }

    // Print result
    for (let key in counts) {
        let result = (counts[key]/numbersCount*100).toFixed(2);
        console.log(`${result}%`);
    }
}

divideWithoutRemainder(["3",
"3",
"6",
"9"]);