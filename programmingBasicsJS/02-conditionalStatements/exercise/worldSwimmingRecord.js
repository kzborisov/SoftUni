// Task 7 - World Swimming Record

function calcTime(input) {
    // Read Input Data
    let recordInSecs = Number(input[0]);
    let distanceInMeters = Number(input[1]);
    let timeInSecsPerMeter = Number(input[2]);

    let neededTime;
    let addedTime;
    let totalTime;
    let result;

    // Calculations
    neededTime = distanceInMeters * timeInSecsPerMeter;
    addedTime = (Math.floor(distanceInMeters / 15)) * 12.5;
    totalTime = neededTime + addedTime;
    Math.abs(totalTime - recordInSecs);

    // Print result
    if (totalTime >= recordInSecs) {
        console.log(`No, he failed! He was ${Math.abs(recordInSecs - totalTime).toFixed(2)} seconds slower.`)
    } else {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`)
    }
}

calcTime(["55555.67",
"3017",
"5.03"]);