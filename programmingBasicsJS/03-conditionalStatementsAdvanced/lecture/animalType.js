// Task 3 - Animal Type

function animalType(input) {
    // Read Input Data
    let animal = input[0];

    // Calculations
    switch (animal) {
        case "dog":
            console.log("mammal");
            break;
        case "crocodile":
        case "tortoise":
        case "snake":
            console.log("reptile");
            break;
        default:
            console.log("unknown");
            break;
    }
}

animalType((["cat"]));