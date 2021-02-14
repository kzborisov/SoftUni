// Task 1 - Seconds Sum

function sumSeconds(input) {
    // Read Input Data
    let timeFirst = Number(input[0]);
    let timeSecond = Number(input[1]);
    let timeThird = Number(input[2]);

    let totalTime;
    let minutes;
    let seconds;
    let result;

    // Calculations
    totalTime = timeFirst + timeSecond + timeThird;
    minutes = Math.floor(totalTime / 60);
    seconds = totalTime % 60;

    // Print result - with a leading 0.
    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`)
    } else {
        console.log(`${minutes}:${seconds}`);
    }
}

sumSeconds(["14", "12",
"10"]);