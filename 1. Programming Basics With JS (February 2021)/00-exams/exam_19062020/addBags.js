// Task 3 - Aluminum Joinery

function aluminumJoinery(input) {
    // Read Input Data
    let joineryCount = Number(input.shift());
    let joineryType = input.shift();
    let delivery = input.shift();

    // Logic
    let price = 0;

    if (joineryCount < 10){
        console.log("Invalid order");
        return;
    }

    switch (joineryType) {
        case "90X130":
            price = 110;
            if (joineryCount > 60){
                price *= 0.92;
            } else if (joineryCount > 30){
                price *= 0.95;
            }
            break;
        case "100X150":
            price = 140;
            if (joineryCount > 80){
                price *= 0.90;
            } else if (joineryCount > 40){
                price *= 0.94;
            }
            break;
        case "130X180":
            price = 190;
            if (joineryCount > 50){
                price *= 0.88;
            } else if (joineryCount > 30){
                price *= 0.93;
            }
            break;
        case "200X300":
            price = 250;
            if (joineryCount > 50){
                price *= 0.86;
            } else if (joineryCount > 25){
                price *= 0.91;
            }
            break;
        default:
            console.error("Error");
            break;
    }

    price *= joineryCount;

    if (delivery === "With delivery"){
        price += 60;
    }

    if (joineryCount > 99){
        price *= 0.96;
    }

    // Print Result
    console.log(`${price.toFixed(2)} BGN`);
}

aluminumJoinery([
    "40",
    "90X130",
    "Without delivery"
]); 