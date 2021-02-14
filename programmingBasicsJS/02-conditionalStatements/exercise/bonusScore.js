// Task 2 - Bonus Score

function bonusScore(input) {
    // Read Input Data
    let score = Number(input[0]);
    let bonus = 0.0;

    // Calculations
    if (score <= 100) {
        bonus = 5;
    } else if (score > 1000) {
        bonus = score * 0.10;
    }
    else if (score > 100) {
        bonus = score * 0.20;
    }

    if (score % 2 === 0) {
        bonus += 1;
    } else if (score % 10 === 5) {
        bonus += 2;
    }

    // Print result - with a leading 0.
    console.log(bonus);
    console.log(score + bonus);

}

bonusScore(["2703"]);