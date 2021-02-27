// Task 3 - Numbers From 1 To N With Step 3

function numbersFromNto1(input) {
    // Read Input
    let num = Number(input[0]);

    // Print Numbers from 1 to N with step 3
    for (var i = 0; i < num; i+=3) {
        console.log(i+1)
    }
}
numbersFromNto1(['10'])