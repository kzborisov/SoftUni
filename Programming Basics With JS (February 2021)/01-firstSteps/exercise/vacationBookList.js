// Task 4 - Vacation Book List
function calcReadingHours(input) {
    let currentBookPages = Number(input[0]);
    let pagesPerHour = Number(input[1]);
    let daysPerHour = Number(input[2]);
    let result = (currentBookPages / pagesPerHour) / daysPerHour;
    console.log(result);
}

calcReadingHours(["432", "15", "4"]);