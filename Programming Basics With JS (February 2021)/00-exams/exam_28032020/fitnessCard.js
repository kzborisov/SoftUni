// Task 7 - Fitness Card 

function fitnessCard(input) {
    // Read Input
    let budget = Number(input.shift());
    let gender = input.shift();  // m (male) or f (female)
    let age = Number(input.shift());
    let sport = input.shift();

    // Logic
    let priceMap = {
        "m": {
            "Gym": 42,
            "Boxing": 41,
            "Yoga": 45,
            "Zumba": 34,
            "Dances": 51,
            "Pilates": 39
        },
        "f": {
            "Gym": 35,
            "Boxing": 37,
            "Yoga": 42,
            "Zumba": 31,
            "Dances": 53,
            "Pilates": 37
        },
    };

    let totalPrice = priceMap[gender][sport];

    if (age <= 19){
        totalPrice *= 0.80;  // 80% discount for students
    }

    // Print Result
    if (totalPrice <= budget){
        console.log(`You purchased a 1 month pass for ${sport}.`);
    } else {
        let money = totalPrice - budget;
        console.log(`You don't have enough money! You need $${money.toFixed(2)} more.`);
    }
}

fitnessCard(["10",
"m",
"50",
"Pilates"])
;