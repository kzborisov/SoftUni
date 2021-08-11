// Task 7 - Working Hours

function workingHours(input) {
    // Read Input Data
    let hour = Number(input[0]);
    let day = input[1];

    // Calculations
    if (hour >= 10 && hour <= 18){
        switch (day) {
            case "Monday":
            case "Tuesday":
            case "Wednesday":
            case "Thursday":
            case "Friday":
            case "Saturday":
                console.log("open");
                break;
            default:
                console.log("closed");
                break;
        }
    } else {
        console.log("closed");
    }
}

workingHours((["11", "Monday"]));
workingHours((["19", "Friday"]));
workingHours((["11", "Sunday"]));
