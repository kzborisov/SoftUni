// Task 6 - Rhombus Of Stars

function drawFig(input) {
    // Read Input
    let n = Number(input.shift());

    // Logic
    for (let row = 0; row <= n; row++) {
        process.stdout.write(" ".repeat(n-row));
        process.stdout.write("*".repeat(row));
        process.stdout.write(" | ");
        process.stdout.write("*".repeat(row));
        process.stdout.write(" ".repeat(n-row));
        console.log("");
    }
}

drawFig(["3"]);