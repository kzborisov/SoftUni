// Task 6 - Histogram

function histogram(input) {
    // Read Input
    let numbersCount = Number(input[0]);

    // Logic
    let counts = {
        'p1': 0,
        'p2': 0,
        'p3': 0,
        'p4': 0,
        'p5': 0,
    };

    for(let i=1; i<=numbersCount; i++) {
        let num = Number(input[i]);

        if (num >= 800) {
            counts['p5']++;
        } else if (num >= 600){
            counts['p4']++;
        } else if (num >= 400){
            counts['p3']++;
        } else if (num >= 200){
            counts['p2']++;
        } else {
            counts['p1']++;
        }
    }

    // Print result
    for (let key in counts) {
        let result = (counts[key]/numbersCount*100).toFixed(2);
        console.log(`${result}%`);
    }
}

histogram(["7",
"800",
"801",
"250",
"199",
"399",
"599",
"799"]);