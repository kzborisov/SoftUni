// Task 9 - House

function drawFig([input]) {
    let n = Number(input);

    let starsCount = 0;

    // Draw the roof
    for (let i = 0; i < Math.floor((n+1) / 2); i++) {
        if (n % 2 == 0){
            starsCount = 2 * (i + 1);
        } else {
            starsCount = 2 * i + 1;
        }

        console.log("-".repeat((n-starsCount)/2) +
                    "*".repeat(starsCount) +
                    "-".repeat((n-starsCount)/2));
    }

    for (let i = 0; i < Math.floor(n / 2); i++) {
        // Draw the house body: |*****| }
        console.log("|" + "*".repeat(n-2) + "|");
    }
}

drawFig(["6"]);