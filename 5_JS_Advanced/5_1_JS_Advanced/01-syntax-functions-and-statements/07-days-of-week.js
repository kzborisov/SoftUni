function dayOfWeek(day) {
    switch (day) {
        case "Monday":
            return 1;
        case "Tuesday":
            return 2;
        case "Wednesday":
            return 3;
        case "Thursday":
            return 4;
        case "Friday":
            return 5;
        case "Saturday":
            return 6;
        case "Sunday":
            return 7;
        default:
            return "error";
    }
}

console.log(dayOfWeek("Monday"));
console.log(dayOfWeek("Tuesday"));
console.log(dayOfWeek("Friday"));
console.log(dayOfWeek("Invalid"));
