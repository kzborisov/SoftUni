// Task 4 - Car Number

function carNumber(input) {
    // Read Input
    let start = Number(input.shift());
    let end = Number(input.shift())

    // Logic
    for (let first = start; first <= end; first++) {
        for(let second = start; second <= end; second++) {
            for(let third = start; third <= end; third++) {
                for(let fourth = start; fourth <= end; fourth++) {
                    // Conditions
                    let isStartingWithEven = first % 2 == 0 && fourth % 2 == 1;
                    let isStartingWithOdd = first % 2 == 1 && fourth % 2 == 0;
                    let isFirstBiggerThanLast = first > fourth;
                    let isSumEven = (second + third) % 2 === 0;
                    if ((isStartingWithEven || isStartingWithOdd) && isFirstBiggerThanLast && isSumEven){
                        process.stdout.write(`${first}${second}${third}${fourth} `);
                    }
                    
                }
            }
        }
    }
}

carNumber(["2", "3"]);