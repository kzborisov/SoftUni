// Task 5 - Journey

function journey(input) {
    // Read Input Data
    let budget = Number(input[0]);
    let season = input[1];

    // Logic
    let destination = "Bulgaria";
    let place = "Camp";
    let sum = 0;

    if (budget <= 100) {
        switch (season) {
            case "summer":
                place = "Camp";
                sum = budget * 0.30;
                break;
            case "winter":
                place = "Hotel";
                sum = budget * 0.70;
                break;
        }
    } else if (budget <= 1000) {
        destination = "Balkans"
        switch (season) {
            case "summer":
                place = "Camp";
                sum = budget * 0.40;
                break;
            case "winter":
                place = "Hotel";
                sum = budget * 0.80;
                break;
        }
    } else if (budget > 1000) {
        destination = "Europe";
        place = "Hotel";
        sum = budget * 0.90;
    }

    // Print Result
    console.log(`Somewhere in ${destination}`);
    console.log(`${place} - ${sum.toFixed(2)}`);
}

journey(["1500", "summer"]);