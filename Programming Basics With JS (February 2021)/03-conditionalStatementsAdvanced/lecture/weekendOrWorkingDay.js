// Task 2 - Weekend Or Working Day

function weekendOrWorkingDay(input) {
    // Read Input Data
    let day = input[0];

    // Calculations
    switch (day) {
        case "Monday":
        case "Tuesday":
        case "Wednesday":
        case "Thursday":
        case "Friday":
            console.log("Working day");
            break;
        case "Saturday":
        case "Sunday":
            console.log("Weekend");
            break;
        default:
            console.log("Error");
            break;
    }
}
weekendOrWorkingDay((["Monday"]));