// Task 1 - Pipes in Pool

function pipesInPool(input) {
    // Read Input Data
    let volumeInLitters = Number(input[0]);
    let P1 = Number(input[1]);  // Flow rate of pipe 1
    let P2 = Number(input[2]);  // Flow rate of pipe 2
    let absentHours = Number(input[3]);

    // Calculations
    let firstPipe = P1 * absentHours;
    let secondPipe =  P2 * absentHours;
    let totalLitters = firstPipe + secondPipe;
    let firstPipeInPercents = (firstPipe / totalLitters) * 100;
    let secondPipeInPercents = (secondPipe / totalLitters) * 100;
    let resultInPercents = (totalLitters / volumeInLitters) * 100;

    // Print result
    if (totalLitters <= volumeInLitters){
        console.log(`The pool is ${resultInPercents.toFixed(2)}% full. Pipe 1: ${firstPipeInPercents.toFixed(2)}%. Pipe 2: ${secondPipeInPercents.toFixed(2)}%.`)
    } else {
        console.log(`For ${absentHours} hours the pool overflows with ${(Math.abs(totalLitters - volumeInLitters)).toFixed(2)} liters.`)
    }
}

pipesInPool(["100", "100", "100", "2.5"])