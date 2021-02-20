// Task 11- Fruit Shop

function fruitShop(input) {
    // Read Input Data
    let product = input[0];
    let day = input[1];
    let quantity = Number(input[2]);

    // Calculations
    let priceMap = {
        "workingDays": {
            "banana": 2.50,
            "apple": 1.20,
            "orange": 0.85,
            "grapefruit": 1.45,
            "kiwi": 2.70,
            "pineapple": 5.50,
            "grapes": 3.85
        },
        "weekend": {
            "banana": 2.70,
            "apple": 1.25,
            "orange": 0.90,
            "grapefruit": 1.60,
            "kiwi": 3.00,
            "pineapple": 5.60,
            "grapes": 4.20
        }
    };

    let result;
    if (!(product in priceMap["workingDays"]) && !(product in priceMap["weekend"])) {
        console.log("error");
        return;
    } else {
        switch (day){
            case "Monday":
            case "Tuesday":
            case "Wednesday":
            case "Thursday":
            case "Friday":
                result = (priceMap["workingDays"][product] * quantity).toFixed(2);
                break;
            case "Saturday":
            case "Sunday":
                result = (priceMap["weekend"][product] * quantity).toFixed(2);
                break;
            default:
                result = "error";
                break;
        }
    }

    // Print Result
    console.log(result)
}

fruitShop((["orange",
"Sunday",
"3"]));
