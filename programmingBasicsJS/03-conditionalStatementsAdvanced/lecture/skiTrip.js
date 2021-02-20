// Task 13 - Ski Trip

function skiTrip(input) {
    // Read Input Data
    let days = Number(input[0]);
    let room = input[1];
    let rating = input[2];

    // Rooms Prices
    let roomForOnePerson = 18.00;
    let apartment = 25.00;
    let presidentApartment = 35.00;

    let price = 0;
    let nights = days - 1;

    // Logic
    if (room == "room for one person"){
        price = nights * roomForOnePerson;
    } else if (room == "apartment") {
        if (nights < 10) {
            price = nights * apartment * 0.70;
        } else if (nights >= 10 && nights <= 15) {
            price = nights * apartment * 0.65;
        } else if (nights >= 15) {
            price = nights * apartment * 0.50;
        }
    } else if (room == "president apartment"){
        if (nights < 10) {
            price = nights * presidentApartment * 0.90;
        } else if (nights >= 10 && nights <= 15) {
            price = nights * presidentApartment * 0.85;
        } else if (nights >= 15) {
            price = nights * presidentApartment * 0.80;
        }
    }

    if (rating == "positive") {
        price = price + (price * 0.25);
    } else if (rating == "negative") {
        price = price - (price * 0.10)
    }

    // Print Result
    console.log(price.toFixed(2));
}

skiTrip((["14",
"apartment",
"positive"]));
