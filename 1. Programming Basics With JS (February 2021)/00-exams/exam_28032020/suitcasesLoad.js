// Task 11 - Suitcases Load 

function suitcasesLoad(input) {
    // Read Input
    let capacity = Number(input.shift());
    let suitcaseVolume = input.shift();

    // Logic
    let suitcasesLoaded = 0;
    let index = 0;

    while (suitcaseVolume !== "End") {
        let baggage = Number(suitcaseVolume);
        index++;

        if (index % 3 === 0) baggage *= 1.10;

        if (capacity - baggage < 0){
            break;
        }
        suitcasesLoaded++;
        capacity -= baggage;

        suitcaseVolume = input.shift();
    }

    // Print Result
    if (suitcaseVolume === 'End') {
        console.log("Congratulations! All suitcases are loaded!");
        console.log(`Statistic: ${suitcasesLoaded} suitcases loaded.`);
    } else {
        console.log("No more space!");
        console.log(`Statistic: ${suitcasesLoaded} suitcases loaded.`);
    }
}

suitcasesLoad(["550",
"100",
"252",
"72",
"End"])
;