// Task 3 - Oscars week In Cinema

function oscarsWeek(input){
    // Read Input
    let name = input.shift();
    let roomType = input.shift();
    let ticketsCount = Number(input.shift());

    // Logic
    let priceMap = {
        "normal": {
            "A Star Is Born": 7.50,
            "Bohemian Rhapsody": 7.35,
            "Green Book": 8.15,
            "The Favourite": 8.75
        },
        "luxury": {
            "A Star Is Born": 10.50,
            "Bohemian Rhapsody": 9.45,
            "Green Book": 10.25,
            "The Favourite": 11.55
        },
        "ultra luxury": {
            "A Star Is Born": 13.50,
            "Bohemian Rhapsody": 12.75,
            "Green Book": 13.25,
            "The Favourite": 13.95
        }
    };

    let result = (priceMap[roomType][name] * ticketsCount).toFixed(2);

    // Print Result
    console.log(`${name} -> ${result} lv.`)
}

oscarsWeek(["A Star Is Born",
"luxury",
"42"])