// Task 2 - Multiplication Table

function multiplicationTable(input) {
    // Read Input
    let num = Number(input[0]);

    // Logic
    for (let i=1; i <= 10; i++) {
        console.log(`${i} * ${num} = ${i*num}`);
    }
}

multiplicationTable(['5'])