// Task 7 - Hotel Room

function hotelRoom(input) {
    // Read Input Data
    let month = input[0];
    let nightsCount = Number(input[1]);

    // Logic
    let studioPrice = 0;
    let apartmentPrice = 0;

    let studioPriceMap = {
        "May": 50,
        "October": 50,
        "June": 75.20,
        "September": 75.20,
        "July": 76,
        "August": 76
    };

    let apartmentPriceMap = {
        "May": 65,
        "October": 65,
        "June": 68.70,
        "September": 68.70,
        "July": 77,
        "August": 77
    };

    studioPrice = nightsCount * studioPriceMap[month];
    apartmentPrice = nightsCount * apartmentPriceMap[month];

    if (nightsCount > 14) {
        if (month === "May" || month === "October") {
            studioPrice *= 0.70;
        } else if (month === "June" || month === "September") {
            studioPrice *= 0.80;
        }
        apartmentPrice *= 0.90;
    } else if (nightsCount > 7) {
        if (month === "May" || month === "October") {
            studioPrice *= 0.95;
        }
    }

    // Print Result
    console.log(`Apartment: ${apartmentPrice.toFixed(2)} lv.`);
    console.log(`Studio: ${studioPrice.toFixed(2)} lv.`);
}

hotelRoom(["June",
"14"]);