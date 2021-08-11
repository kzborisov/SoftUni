function godlMine(input) {
    // Read Input
    let locations = Number(input.shift());



    // Logic
    for (let i = 1; i <= locations; i++) {
        let expectedYield = Number(input.shift());
        let days = Number(input.shift());
        let average = 0;

        for (let i = 1; i <= days; i++) {
            let yield = Number(input.shift());
            average += yield;
        }
        average /= days;

        if (average >= expectedYield) {
            console.log(`Good job! Average gold per day: ${average.toFixed(2)}.`);
        } else {
            let diff = expectedYield - average;
            console.log(`You need ${diff.toFixed(2)} gold.`)
        }
    }
}

godlMine(["1",
"5",
"3",
"10",
"1",
"3"]);