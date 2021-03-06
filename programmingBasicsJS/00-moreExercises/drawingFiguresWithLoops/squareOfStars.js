// Task 3 - Square stars

function drawFigure(input) {
    // Read Input
    let n = Number(input.shift());

    // Logic
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            process.stdout.write("* ");
        }
        console.log('');
    }
}

drawFigure(["3"]);