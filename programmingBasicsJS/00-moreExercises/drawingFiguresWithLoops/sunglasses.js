// Task 8 - Sunglasses

function drawFig(input) {
    let n = Number(input.shift());

    console.log('*'.repeat(2 * n) + ' '.repeat(n) + '*'.repeat(2 * n));
    for (let row = 1; row <= n - 2; row++) {
        let middle = (row === Math.ceil((n - 2) / 2) ? '|' : ' ').repeat(n);
        console.log(`*${'/'.repeat(2 * n - 2)}*${middle}*${'/'.repeat(2 * n - 2)}*`);
    }
    console.log('*'.repeat(2 * n) + ' '.repeat(n) + '*'.repeat(2 * n));
}

drawFig(["3"]);