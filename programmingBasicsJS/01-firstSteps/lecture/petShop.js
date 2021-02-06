// Task 8
function calculatePrice(input) {
    let dogsCount = Number(input[0]);
    let otherCount = Number(input[1]);
    let dogsPrice = 2.50;
    let otherPrice = 4;
    let result = (dogsCount * dogsPrice) + (otherCount * otherPrice);
    console.log(`${result} lv.`);
}

calculatePrice(["13", "9"]);