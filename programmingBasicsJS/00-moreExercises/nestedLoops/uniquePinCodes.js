// Task 1 - Unique Pin Codes

function uniquePinCodes(input) {
    // Read Input
    let firstUpperBound = Number(input.shift());
    let secondUpperBound = Number(input.shift());
    let thirdUpperBound = Number(input.shift());

    // Logic
    for (let i = 1; i <= firstUpperBound; i++) {
        for (let j = 2; j <= secondUpperBound; j++){
            for (let k = 1; k <= thirdUpperBound; k++){
                if (i % 2 == 0 && k % 2 == 0 && j <= 7 && j != 4 && j != 6){
                    console.log(`${i} ${j} ${k}`);
                }
            }
        }
    }
}

uniquePinCodes(["3", "5", "5"]);