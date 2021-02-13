// Task 4 - Nums between 100 and 200

function numCheck(input) {
    // Read Input Data
    let num1 = Number(input[0]);
    let result;

    // Calculations
    if (num1 < 100) {
        result = 'Less than 100';
    }
    else if (num1 > 200) {
        result = 'Grater than 200'; 
    } else {
        result = 'Between 100 and 200';
    }
    // Print result formated to .00
    console.log(result);
}

numCheck(["100"]);