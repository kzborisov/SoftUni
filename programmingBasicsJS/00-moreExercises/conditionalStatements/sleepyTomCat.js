// Task 2 - Sleepy Tom Cat

function sleepyTomCat(input) {
    // Read Input Data
    let vacationDays = Number(input[0]);

    let yearlyPlay = 30000; // Minutes

    // Calculations
    // Play time
    let playWhenFree = vacationDays * 127; // In Minutes
    let playWhenWorking = (365 - vacationDays) * 63; // In Minutes
    let totalPlayTime = playWhenFree + playWhenWorking;

    // Print result
    if (totalPlayTime > yearlyPlay) {
        let timeLeft = totalPlayTime - yearlyPlay;
        let H = Math.floor(timeLeft / 60);
        let M = timeLeft % 60;
        console.log("Tom will run away");
        console.log(`${H} hours and ${M} minutes more for play`)
    } else {
        let timeLeft = yearlyPlay - totalPlayTime;
        let H = Math.floor(timeLeft / 60);
        let M = timeLeft % 60;
        console.log("Tom sleeps well");
        console.log(`${H} hours and ${M} minutes less for play`)
    }
}

sleepyTomCat(["20"])