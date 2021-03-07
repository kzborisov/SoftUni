// Task 4 - Triangle of Dollars

function drawFigure(input) {
    // Read Input
    let n = Number(input.shift());

    // Logic
    for (let row = 1; row <= n; row++) {
        for (let col = 1; col <= row; col++) {
            process.stdout.write("$ ");
        }
        console.log('');
    }
}

drawFigure(["3"]);