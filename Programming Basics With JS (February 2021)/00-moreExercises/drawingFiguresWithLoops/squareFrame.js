// Task 5 - Square Frame

function drawFigure(input) {
    let n = Number(input.shift());

    console.log("+ " + "- ".repeat(n-2) + "+");

    for (let i = 0; i < n-2; i++) {
        console.log("| " + "- ".repeat(n-2) + "|");
    }

    console.log("+ " + "- ".repeat(n-2) + "+");
}

drawFigure(["3"]);