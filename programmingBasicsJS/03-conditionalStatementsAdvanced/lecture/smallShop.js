// Task 5 - Small Shop

function smallShop(input) {
    // Read Input Data
    let product = input[0];
    let town = input[1];
    let quantity = Number(input[2]);

    // Calculations
    let productMap = {
        'Sofia': {
            "coffee": 0.50,
            "water": 0.80,
            "beer": 1.20,
            "sweets": 1.45,
            "peanuts": 1.60
        },
        'Plovdiv': {
            "coffee": 0.40,
            "water": 0.70,
            "beer": 1.15,
            "sweets": 1.30,
            "peanuts": 1.50
        },
        'Varna': {
            "coffee": 0.45,
            "water": 0.70,
            "beer": 1.10,
            "sweets": 1.35,
            "peanuts": 1.55
        }
    };

    // Print Result
    console.log(productMap[town][product] * quantity);
}

smallShop((["peanuts", "Plovdiv", "1"]));