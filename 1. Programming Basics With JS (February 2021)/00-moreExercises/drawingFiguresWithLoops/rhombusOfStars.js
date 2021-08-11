// Task 6 - Rhombus Of Stars

function drawFig(input) {
    // Read Input
    let n = Number(input.shift());

    // Logic
    for (let i = 1; i <= n; i++) {
        console.log(" ".repeat(n-i) + "* ".repeat(i) + " ".repeat(n-i));
    }
    for (let i = n-1; i >= 1; i--) {
        console.log(" ".repeat(n-i) + "* ".repeat(i) + " ".repeat(n-i));
    }
}

drawFig(["3"]);