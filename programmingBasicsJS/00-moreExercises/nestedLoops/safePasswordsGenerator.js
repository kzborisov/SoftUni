// Task 7 - Safe Passwords Generators

function safePasswordsGenerator(input) {
    // Read Input
    let a = Number(input.shift());
    let b = Number(input.shift());
    let maxPasswords = Number(input.shift());

    // Logic
    let totalCombinations = 0;
    let firstAndLast = 35;
    let secondAndBeforeLast = 64;

    for (let i = 1; i <= a; i++) {
        for (let j = 1; j <= b; j++) {
            totalCombinations++;
            if (totalCombinations > maxPasswords)
            {
                break;
            }
            if (firstAndLast > 55){
                firstAndLast = 35;
            }
            if (secondAndBeforeLast > 96){
                secondAndBeforeLast = 64;
            }
            process.stdout.write(`${String.fromCharCode(firstAndLast)}${String.fromCharCode(secondAndBeforeLast)}${i}${j}${String.fromCharCode(secondAndBeforeLast)}${String.fromCharCode(firstAndLast)}|`)
            firstAndLast++;
            secondAndBeforeLast++;
        }
    }
}

safePasswordsGenerator(["2", "3", "10"]);