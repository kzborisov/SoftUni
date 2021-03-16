// Task 3 - Cat Walking 

function catWalking(input) {
    // Read Input
    let walkingMinutes = Number(input.shift());  // Per day
    let walkingCount = Number(input.shift());    // Per day
    let calories = Number(input.shift());        // Per day

    // Logic

    let totalWalkingTime = walkingMinutes * walkingCount;
    let caloriesBurned = totalWalkingTime * 5;  // 5 calories per minute
    let halfCalories = calories / 2;

    // Print Result
    if (caloriesBurned >= halfCalories) {
        console.log(`Yes, the walk for your cat is enough. Burned calories per day: ${caloriesBurned}.`);
    } else {
        console.log(`No, the walk for your cat is not enough. Burned calories per day: ${caloriesBurned}.`);
    }
}

catWalking(["15",
"2",
"500"]);