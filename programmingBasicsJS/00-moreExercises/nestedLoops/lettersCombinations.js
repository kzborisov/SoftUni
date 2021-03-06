// Task 2 - Letters Combinations

function lettersCombinations(input) {
    // Read Input
    let firstLetter = input.shift();
    let secondLetter = input.shift();
    let skipLetter = input.shift();

    // Logic
    let combinations = 0;
    let start = firstLetter.charCodeAt(0);
    let end = secondLetter.charCodeAt(0)

    for (let i = start; i <= end; i++) {
        if (String.fromCharCode(i) === skipLetter){
            continue;
        }
        for (let j = start; j <= end; j++) {
            if (String.fromCharCode(j) === skipLetter){
                continue;
            }
            for (let k = start; k<= end; k++){
                if (String.fromCharCode(k) != skipLetter){
                    combinations++;
                    process.stdout.write(`${String.fromCharCode(i)}${String.fromCharCode(j)}${String.fromCharCode(k)} `);
                }
            }
        }
    }

    console.log(combinations);
}

lettersCombinations(["a", "c", "b"]);