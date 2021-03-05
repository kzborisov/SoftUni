// Task 1 - Back To The Past

function backToThePast(input) {
    // Read Input
    let inheritance = Number(input[0]);
    let endYear = Number(input[1]);

    let startYear = 1800;
    let age = 18;

    // Logic
    for(let i=startYear; i <= endYear; i++){
        if (i % 2 == 0){
            inheritance -= 12000;
        } else {
            inheritance -= 12000 + age * 50;
        }
        age++;
    }

    // Print Result
    if (inheritance < 0){
        console.log(`He will need ${Math.abs(inheritance).toFixed(2)} dollars to survive.`)
    } else {
        console.log(`Yes! He will live a carefree life and will have ${inheritance.toFixed(2)} dollars left.`)
    }
}

backToThePast(["12000",
"1800"]);