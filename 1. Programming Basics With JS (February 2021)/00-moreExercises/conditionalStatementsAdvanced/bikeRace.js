// Task 2 - Bike Race

function bikeRace(input) {
    // Read Input Data
    let juniorsCount = Number(input[0]);
    let seniorsCount = Number(input[1]);
    let traceType = input[2];

    // Logic
    let priceMap = {
        'juniors': {
            'trail': 5.50,
            'cross-country': 8,
            'downhill': 12.25,
            'road': 20
        },
        'seniors': {
            'trail': 7,
            'cross-country': 9.50,
            'downhill': 13.75,
            'road': 21.50
        }
    };

    let totalSum = (priceMap["juniors"][traceType] * 
    juniorsCount + priceMap["seniors"][traceType] * seniorsCount) * 0.95;

    if (traceType.toLowerCase() === 'cross-country' && (juniorsCount + seniorsCount) >= 50) {
        totalSum *= 0.75;
    }
    // Print Result
    console.log(totalSum.toFixed(2));
}

bikeRace(["10",
"10",
"cross-country"]);
