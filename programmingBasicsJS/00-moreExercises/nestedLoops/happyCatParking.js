// Task 11 - Happy Cat Parking

function happyCatParking(input) {
    // Read Input
    let days = Number(input.shift());
    let hoursPerDay = Number(input.shift());

    // Logic
    let totalSum = 0;

    for (let day = 1; day <= days; day++) {
        let sum = 0;
        for (let hour = 1; hour <= hoursPerDay; hour++) {
            if (day % 2 === 0 && hour % 2 != 0){
                sum += 2.50;
            } else if (day % 2 != 0 && hour % 2 === 0){
                sum += 1.25;
            } else {
                sum += 1;
            }
        }
        totalSum += sum;
        
        console.log(`Day: ${day} - ${sum.toFixed(2)} leva`);
    }
    console.log(`Total: ${totalSum.toFixed(2)} leva`);
}

happyCatParking(["2", "5"]);