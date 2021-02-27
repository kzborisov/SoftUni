// Task 1 - Match TIckets

function matchTickets(input) {
    // Read Input Data
    let budget = Number(input[0]);
    let category = input[1];
    let people = Number(input[2]);

    // Logic
    let transportPrice = 0;

    let ticketPriceMap = {
        'VIP': 499.99,
        'Normal': 249.99
    };

    if (people >= 1 && people <= 4) {
        transportPrice = budget * 0.75;
    } else if (people >= 5 && people <= 9) {
        transportPrice = budget * 0.60;
    } else if (people >= 10 && people <= 24) {
        transportPrice = budget * 0.50;
    } else if (people >= 25 && people <= 49) {
        transportPrice = budget * 0.40;
    } else {
        transportPrice = budget * 0.25
    }

    let ticketPrice = ticketPriceMap[category] * people;
    let moneyLeft = budget - transportPrice;

    // Print Result
    if (ticketPrice <= moneyLeft){
        console.log(`Yes! You have ${(moneyLeft - ticketPrice).toFixed(2)} leva left.`)
    } else {
        console.log(`Not enough money! You need ${(ticketPrice - moneyLeft).toFixed(2)} leva.`)
    }
}

matchTickets(["30000",
"VIP",
"49"]);
