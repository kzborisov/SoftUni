// Task 8 - Equal Pairs

function equalPairs(input) {
    // Read Input
    let pairsCount = Number(input.shift());

    // Logic
    let lastPair = 0;
    let maxDiff = 0;

    for (let i = 0; i < pairsCount; i++) {
        let num = Number(input.shift());
        let num2 = Number(input.shift());

        let currentPair = num + num2;
        
        if (i > 0){
            let diff = Math.abs(currentPair - lastPair);
            if (diff > maxDiff){
                maxDiff = diff;
            }
        }

        lastPair = currentPair;
    }

    // Print Result
    if (maxDiff === 0) {
        console.log(`Yes, value=${lastPair}`);
    } else {
        console.log(`No, maxdiff=${maxDiff}`);
    }
}

equalPairs(["7",
    "34",
    "-33",
    "52",
    "12",
    "-32",
    "32",
    "23",
    "41",
    "7",
    "25",
    "34",
    "23",
    "124",
    "21",]);