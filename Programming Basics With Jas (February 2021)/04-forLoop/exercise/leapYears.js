// Task 3 - Leap Years

function leapYears(input) {
    // Read Input
    let startYear = Number(input[0]);
    let endYear = Number(input[1]);

    // Logic
    for (let i=startYear; i<=endYear; i+=4) {
        console.log(i);
    }
}

leapYears(["1908",
"1919"]);