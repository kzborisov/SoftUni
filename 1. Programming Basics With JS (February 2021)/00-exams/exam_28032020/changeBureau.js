// Task 1 - Change Bureau

function changeBureau(input) {
    // Read Input
    let bitcoinCount = Number(input.shift());
    let yuansCount = Number(input.shift());
    let commission = Number(input.shift());

    // Logic
    let priceMap = {
        'bitcoin': 1168, // leva
        'yuna': 0.15,   // dollars
        'dollar': 1.76,  // leva
        'euro': 1.95    // leva
    };

    let bitcoin = priceMap['bitcoin'] * bitcoinCount;
    let yuans = priceMap['yuna'] * yuansCount * priceMap['dollar'];
    let total = (bitcoin + yuans) / priceMap['euro'];
    total *= (1 - (commission / 100));  // commission 

    // Print Result
    console.log(total.toFixed(2));
}

changeBureau(["20",
"5678",
"2.4"]);