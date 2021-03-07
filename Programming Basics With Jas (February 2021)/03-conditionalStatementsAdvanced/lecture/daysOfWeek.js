// Task 1 - Days Of Week

function weekDays(input) {
    // Read Input Data
    let num = Number(input[0]);

    // Calculations
    let daysMap = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    };

    // Print result
    if (num in daysMap){
        console.log(daysMap[num]);
    } else {
        console.log("Error");
    }
}

weekDays((["-1"]));