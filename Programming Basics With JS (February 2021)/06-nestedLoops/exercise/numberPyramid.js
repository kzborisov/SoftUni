// Task 1 - Number Pyramid

function numberPyramid(input) {
    // Read Input
    let num = Number(input.shift());

    // Logic
    let current = 1;

    for (let row = 1; row <= num; row++){
        for (let col = 1; col <= row; col++){
            if (current > num){
                break;
            }
            process.stdout.write(`${current} `);
            current++;
        }
        console.log();
    }
}

numberPyramid(["15"]);