// Task 5 - Special Numbers

function specialNumbers(input) {
    // Read Input
    let num = Number(input.shift());

    // Logic
    for (let first = 1; first < 9; first++){
        if (num % first == 0){
            for (let second = 1; second < 9; second++){
                if (num % second == 0){
                    for (let third = 1; third < 9; third++){
                        if (num % third == 0){
                            for (let fourth = 1; fourth < 9; fourth++){
                                if (num % fourth == 0){
                                    process.stdout.write(`${first}${second}${third}${fourth} `);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

specialNumbers(["3"]);