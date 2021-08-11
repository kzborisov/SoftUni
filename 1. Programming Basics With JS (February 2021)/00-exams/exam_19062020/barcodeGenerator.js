// Task 6 - Barcode Generator

function bestPlayer(input) {
    // Read Input
    let start = input.shift();
    let end = input.shift();

    // Logic
    for (let i = start[0]; i <= end[0]; i++) {
        if (i % 2 != 0){
            for (let j = start[1]; j <= end[1]; j++){
                if (j % 2 != 0){
                    for (let k = start[2]; k <= end[2]; k++){
                        if (k % 2 != 0){
                            for (let l = start[3]; l <= end[3]; l++){
                                if (l % 2 != 0){
                                    process.stdout.write(`${i}${j}${k}${l} `);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

bestPlayer(["2345",
"6789"]);