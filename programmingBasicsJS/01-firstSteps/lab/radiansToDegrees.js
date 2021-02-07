// Task 2 - Radians to Degrees Convert
function radToDeg(input) {
    let rad = Number(input[0]);
    let result = rad *180 / Math.PI;
    console.log(result.toFixed(0));
}

radToDeg(["6.2832"]);