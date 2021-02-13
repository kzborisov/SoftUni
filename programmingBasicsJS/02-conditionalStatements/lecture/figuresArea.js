// Task 6 - Figures Area

function calcArea(input) {
    // Read Input Data
    let figure = input[0];
    let result;

    // Calculations
    if (figure == 'square') {
        let side = Number(input[1]);
        result = side * side;
    } else if (figure == 'rectangle') {
        let sideA = Number(input[1]);
        let sideB = Number(input[2]);
        result = sideA * sideB;
    } else if (figure == 'circle') {
        let r = Number(input[1]);
        result = Math.PI * Math.pow(r, 2);
    } else if (figure == 'triangle') {
        let side = Number(input[1]);
        let height = Number(input[2]);
        result = (side * height) / 2;
    }

    // Print result formated to .000
    console.log(result.toFixed(3));
}

calcArea(["triangle",
"4.5",
"20"]);