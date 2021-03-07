// Task 4 - Transport Price

function transportPrice(input) {
    // Read Input Data
    let kilometers = Number(input[0]);
    let dayOrNight = input[1];

    let ride;
    let price = 0;

    // Calculations
    if (kilometers >= 100){
        ride = 'train';
    } else if (kilometers < 20){
        ride = 'taxi';
        price += 0.70;
    } else if (kilometers < 100){
        ride = 'bus';
    }

    let dictMap = {
        "taxi_day": 0.79,
        "taxi_night": 0.90,
        "bus_day": 0.09,
        "bus_night": 0.09,
        "train_day": 0.06,
        "train_night": 0.06,
    };

    price += dictMap[ride + "_" + dayOrNight] * kilometers;

    // Print result
    console.log(price.toFixed(2));
}

transportPrice(["7", "night"]);