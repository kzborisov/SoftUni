// Task 1 - Cinema

function cinema(input) {
    // Read Input Data
    let type = input[0];
    let rows = Number(input[1]);
    let colums = Number(input[2]);

    // Logic
    let priceMap = {
        "Premiere": 12.00,
        "Normal": 7.50,
        "Discount": 5.00
    };

    // Print Result
    let totalMoney = (priceMap[type] * rows * colums).toFixed(2);
    console.log(`${totalMoney} leva`);
}

cinema(["Normal",
"21",
"13"]);
