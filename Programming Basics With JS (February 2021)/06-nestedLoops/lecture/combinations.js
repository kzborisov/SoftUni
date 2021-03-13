// Task 3 - Combinations

function combinations(input) {
    // Read Input
    let n = Number(input.shift());

    // Logic
    let count = 0;
    for (let i = 0; i <= n; i++) {
        for (let j = 0; j <= n; j++) {
            for (let k =0 ; k <= n; k++){
                if (i + j + k === n){
                    count++;
                }
            }
        }
    }

    // Print result
    console.log(count);
}

combinations(["5"]);