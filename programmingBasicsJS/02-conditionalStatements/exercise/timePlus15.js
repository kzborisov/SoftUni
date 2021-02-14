// Task 5 - Time + 15

function timePlust15(input) {
    // Read Input Data
    let hoursInput = Number(input[0]);
    let minutesInput = Number(input[1]);

    let totalTime;
    let hoursToMinutes;
    let hours;
    let minutes;

    // Calculations
    hoursToMinutes = hoursInput * 60;
    totalTime = hoursToMinutes + minutesInput + 15;

    hours = Math.floor(totalTime / 60);
    minutes = totalTime % 60;
    if (minutes > 60) {
        hours += 1;
    }
    if (hours >= 24) {
        hours = hours - 24;
    }

    // Print result
    if (minutes < 10) {
        console.log(`${hours}:0${minutes}`);
    } else {
        console.log(`${hours}:${minutes}`)
    }
    
}

timePlust15(["12", "49"]);