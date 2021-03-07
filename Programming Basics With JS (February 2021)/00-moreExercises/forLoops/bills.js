// Task 6 - Bills

function bills(input) {
    // Read Input
    let months = Number(input[0]);

    // Logic
    let billsPriceMap = {
        "Electricity:": 0,
        "Water:": 0,
        "Internet:": 0,
        "Other:": 0
    };
    let average = 0;

    for (let i = 1; i <= months; i++) {
        let electricityBill = Number(input[i]);

        billsPriceMap["Electricity:"] += electricityBill;
        billsPriceMap["Water:"] += 20;
        billsPriceMap["Internet:"] += 15;
        let total = electricityBill + 20 + 15;
        billsPriceMap["Other:"] +=  total + total * 0.2;
    }

    // Print Result
    for (key in billsPriceMap) {
        console.log(`${key} ${billsPriceMap[key].toFixed(2)} lv`);
        average += billsPriceMap[key];
    }
    console.log(`Average: ${(average/months).toFixed(2)} lv`);
}

bills(["5",
    "68.63",
    "89.25",
    "132.53",
    "93.53",
    "63.22"]);