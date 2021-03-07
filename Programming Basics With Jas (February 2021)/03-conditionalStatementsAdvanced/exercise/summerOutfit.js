// Task 2 - Summer Outfit

function summerOutfit(input) {
    // Read Input Data
    let degrees = Number(input[0]);
    let timeOfDay = input[1];

    // Logic
    let outfit = "";
    let shoes = "";
    if (degrees >= 10 && degrees <= 18) {
        switch (timeOfDay) {
            case "Morning":
                outfit = "Sweatshirt";
                shoes = "Sneakers";
                break;
            case "Afternoon":
            case "Evening":
                outfit = "Shirt";
                shoes = "Moccasins";
                break;
            default:
                break;
        }
    } else if (degrees > 18 && degrees <= 24) {
        switch (timeOfDay) {
            case "Morning":
            case "Evening":
                outfit = "Shirt";
                shoes = "Moccasins";
                break;
            case "Afternoon":
                outfit = "T-Shirt";
                shoes = "Sandals";
                break;
            default:
                break;
        }
    } else if (degrees >= 25) {
        switch (timeOfDay) {
            case "Morning":
                outfit = "T-Shirt";
                shoes = "Sandals";
                break;
            case "Afternoon":
                outfit = "Swim Suit";
                shoes = "Barefoot";
                break;
            case "Evening":
                outfit = "Shirt";
                shoes = "Moccasins";
                break;
            default:
                break;
        }
    }

    // Print Result
    console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`)
}

summerOutfit(["25",
"Morning"]);
