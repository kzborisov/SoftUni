// Task 9 - Trekking Mania 

function trekkingMania(input) {
    // Read Input
    let groups = Number(input.shift());

    // Logic
    let totalCount = 0;
    let musala = 0;
    let monblan = 0;
    let kilimanjaro = 0;
    let k2 = 0;
    let everest = 0;

    for (let group = 1; group <= groups; group++){
        let people = Number(input.shift());
        totalCount += people;

        if (people >= 41) everest += people;
        else if (people >= 26) k2 += people;
        else if (people >= 13) kilimanjaro += people;
        else if (people >= 6) monblan += people;
        else musala += people;
    }

    // Print Result
    console.log(`${((musala / totalCount) * 100).toFixed(2)}%`)
    console.log(`${((monblan / totalCount) * 100).toFixed(2)}%`)
    console.log(`${((kilimanjaro / totalCount) * 100).toFixed(2)}%`)
    console.log(`${((k2 / totalCount) * 100).toFixed(2)}%`)
    console.log(`${((everest/ totalCount) * 100).toFixed(2)}%`)
}

trekkingMania(["10",
"10",
"5",
"1",
"100",
"12",
"26",
"17",
"37",
"40",
"78"])
;