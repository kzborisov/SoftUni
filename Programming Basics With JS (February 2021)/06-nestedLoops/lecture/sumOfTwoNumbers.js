// Task 4 - Sum Of Two Numbers

function sumOfTwoNumbers(input) {
    // Read Input
    let start = Number(input.shift());
    let end = Number(input.shift());
    let magicNumber = Number(input.shift());

    // Logic
    let count = 0;
    for (let first = start; first <= end; first++) {
        for (let second = start; second <= end; second++) {
            count++;
            if (first + second === magicNumber){
                console.log(`Combination N:${count} (${first} + ${second} = ${magicNumber})`);
                return;
            }
        }
    }

    // Print result
    console.log(`${count} combinations - neither equals ${magicNumber}`);
}

sumOfTwoNumbers(["88", 
"888", 
"2000"])