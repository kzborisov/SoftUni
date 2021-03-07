// Task 13 - Prime Pairs

function primePairs(input) {
    // Read Input
    let firstStart = Number(input.shift());
    let secondStart = Number(input.shift());
    let firstDiff = Number(input.shift());
    let secondDiff = Number(input.shift());

    // Logic
    for (let i = firstStart; i<= firstStart + firstDiff; i++) {
        for (let j = secondStart; j <= secondStart + secondDiff; j++){
            let isFirstNumPrime = true;
            let isSecondNumPrime = true;
            for (let k = 2; k <= Math.sqrt(i); k++) {
                if ( i % k == 0) {
                    isFirstNumPrime = false;
                    break;
                }
            }
            for (let k = 2; k <= Math.sqrt(j); k++) {
                if ( j % k == 0) {
                    isSecondNumPrime = false;
                    break;
                }
            }
            if (isFirstNumPrime && isSecondNumPrime) {
                console.log(`${i}${j}`)
            }
        }
    }
}

primePairs(["10", "20", "5", "5"]);