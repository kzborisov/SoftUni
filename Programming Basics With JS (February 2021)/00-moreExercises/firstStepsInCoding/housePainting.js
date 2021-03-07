// Task 7 - Fishland
function calcNeededMoney(input) {
    // Read Input Data
    let height = Number(input[0]);
    let length = Number(input[1]);
    let rooftopHeight = Number(input[2]);

    // Initialize variables
    let side;
    let window;
    let bothSides;
    let backSide;
    let fronAndBackSide;
    let totalArea;
    let rooftop;
    let greenPaint;
    let redPaint;

    // Calculations
    side = height * length;
    window = 1.5 * 1.5;
    bothSides = 2 * side - 2 * window;
    backSide = (height * height);
    fronAndBackSide= (backSide * 2) - 1.2 * 2; // 1.2*2 for the entrance
    totalArea = bothSides + fronAndBackSide; // Square metres
    rooftop = (2 * (height * length)) + (2 * (height * rooftopHeight/2));


    greenPaint = totalArea / 3.4;
    redPaint = rooftop / 4.3;

    // Print result formated to .00
    console.log(greenPaint.toFixed(2))
    console.log(redPaint.toFixed(2));
}

calcNeededMoney(["10.25", "15.45", "8.88"]);