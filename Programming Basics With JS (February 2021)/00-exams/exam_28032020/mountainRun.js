// Task 4 - Mountain Run 

function mountainRun(input) {
    // Read Input
    let record = Number(input.shift());           // In seconds
    let distance = Number(input.shift());         // In meters
    let timeForOneMeter = Number(input.shift());  // In seconds

    // Logic

    let time = distance * timeForOneMeter;
    let additionalTime = Math.floor((distance / 50)) * 30;  // 30 seconds every 50 meters
    let totalTime = time + additionalTime;

    // Print Result
    if (totalTime < record) {
        console.log(`Yes! The new record is ${totalTime.toFixed((2))} seconds.`);
    } else {
        let diff = totalTime - record;
        console.log(`No! He was ${diff.toFixed(2)} seconds slower.`);
    }
}

mountainRun(["5554.36",
"1340",
"3.23"]);