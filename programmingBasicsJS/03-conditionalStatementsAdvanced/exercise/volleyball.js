// Task 9 - Volleyball

function volleyball(input) {
    // Read Input Data
    let yearType = input[0];
    let holidays = Number(input[1]);
    let weekendsAtHome = Number(input[2]);

    // Logic
    let saturdayGames = (48 - weekendsAtHome) * (3/4);
    let sundayGames = weekendsAtHome;
    let holidayGames = holidays * (2/3);
    let totalGames = saturdayGames + sundayGames + holidayGames;

    if (yearType === "leap") {
        totalGames += totalGames *  0.15;
    }

    // Print Result
    console.log(Math.floor(totalGames));
}

volleyball(["normal",
"6",
"13"]);