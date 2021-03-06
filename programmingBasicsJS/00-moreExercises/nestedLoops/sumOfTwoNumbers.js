// Task 9 - Sum of Two Numbers

function sumOfTwoNumbers(input) {
    // Read Input
    let start = Number(input.shift());
    let end = Number(input.shift());
    let magicNumber = Number(input.shift());

    // Logic
    let combination = 0;
    let isFound = false;
    let data = []

    for (let i = start; i <= end; i++){
        if (!isFound){
            for (let j = start; j <= end; j++){
                combination++;
                if (i + j == magicNumber){
                    isFound = true;
                    data[0] = combination;
                    data[1] = i;
                    data[2] = j;
                }
            }
        }
    }
    if (isFound){
        console.log(`Combination N:${data[0]} (${data[1]} + ${data[2]} = ${magicNumber})`);
    } else {
        console.log(`${combination} combinations - neither equals ${magicNumber}`);
    }
}

sumOfTwoNumbers(["1", "10", "5"]);