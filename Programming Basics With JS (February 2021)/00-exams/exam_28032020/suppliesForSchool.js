// Task 2 - Supplies For School

function supplyForSchool(input) {
    // Read Input
    let penBoxCount = Number(input.shift());
    let markerBoxCount = Number(input.shift());
    let cleaningSprayL = Number(input.shift());
    let discount = Number(input.shift());

    // Logic
    let priceMap = {
        'penBox': 5.80,     // leva
        'markerBox': 7.20,  // dollars
        'cleaner': 1.20     // leva per littre
    };

    let penBox = priceMap['penBox'] * penBoxCount;
    let markerBox = priceMap['markerBox'] * markerBoxCount;
    let cleaningSpray = priceMap['cleaner'] * cleaningSprayL;
    let total = penBox + markerBox + cleaningSpray;
    total *= (1 - (discount / 100));  // commission 

    // Print Result
    console.log(total.toFixed(3));
}

supplyForSchool(["4",
"2",
"5",
"13"]);