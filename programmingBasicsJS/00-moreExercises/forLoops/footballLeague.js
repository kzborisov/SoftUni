// Task 7 - Football League

function footballLeague(input) {
    // Read Input
    let staduimCapacity = Number(input[0]);
    let fansCount = Number(input[1]);

    // Logic
    let sectorMap = {
        "A": 0,
        "B": 0,
        "V": 0,
        "G": 0
    };

    for (let i = 1; i <= fansCount; i++) {
        let sector = input[i+1];
        sectorMap[sector]++;
    }

    // Print Result
    for (key in sectorMap) {
        console.log(`${(sectorMap[key]/fansCount*100).toFixed(2)}%`);
    }
    console.log(`${(fansCount/staduimCapacity*100).toFixed(2)}%`);
}

footballLeague(["76",
    "10",
    "A",
    "V",
    "V",
    "V",
    "G",
    "B",
    "A",
    "V",
    "B",
    "B"]);