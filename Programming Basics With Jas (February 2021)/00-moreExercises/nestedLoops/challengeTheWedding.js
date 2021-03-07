// Task 5 - Challenge The Wedding

function challengeTheWedding(input) {
    // Read Input
    let menCount = Number(input.shift());
    let womenCount = Number(input.shift());
    let maxTables = Number(input.shift());

    // Logic
    for(let men = 1; men <= menCount; men++) {
        for(let women = 1; women <= womenCount; women++) {
            if (maxTables <= 0){
                return;
            }

            process.stdout.write(`(${men} <-> ${women}) `);
            maxTables--;
        }
    }
}

challengeTheWedding(["2", "2", "3"]);