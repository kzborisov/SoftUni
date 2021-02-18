// Task 5 - Firm

function firm(input) {
    // Read Input Data
    let hoursNeeded = Number(input[0]);
    let days = Number(input[1]);
    let overtimeCountEmployees = Number(input[2]);

    // Calculations
    let workingHours = 0.90 * days * 8; // Days - 10% * 8 hours/day
    let overtime = overtimeCountEmployees * (2 * days);  // 3 employes * 2 additional hours per day
    let totalHours = Math.floor(workingHours + overtime);

    // Print result
    if (totalHours >= hoursNeeded) {
        console.log(`Yes!${totalHours - hoursNeeded} hours left.`)
    } else {
        console.log(`Not enough time!${hoursNeeded- totalHours} hours needed.`)
    }
}

firm(["99", "3", "1"]);