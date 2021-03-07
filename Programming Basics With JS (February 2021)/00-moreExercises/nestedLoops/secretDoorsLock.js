// Task 8 - Secret Door's Lock

function secretDoorsLock(input) {
    // Read Input
    let hundresUpperBoundary = Number(input.shift());
    let tensUpperBoundary = Number(input.shift());
    let onesUpperBoundary = Number(input.shift());

    // Logic
    for (let hundreds = 1;hundreds<= hundresUpperBoundary; hundreds++) {
        if (hundreds % 2 == 0) {
            for (let tens = 2; tens<= tensUpperBoundary; tens++) {
                if (tens <= 7 && tens != 4 && tens != 6){
                    for (let ones = 1; ones<= onesUpperBoundary; ones++) {
                        if (ones % 2 == 0) {
                            console.log(`${hundreds} ${tens} ${ones}`);
                        }
                    }
                }
            }
        }
    }
}

secretDoorsLock(["3", "5", "5"]);