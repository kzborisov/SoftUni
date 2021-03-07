// Task 6 - Operations Between Numbers

function operationsBetweenNumbers(input) {
    // Read Input Data
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);
    let operator = input[2];

    // Logic
    let equation = `${num1} ${operator} ${num2}`;
    let result = eval(equation);
    let isEven = result % 2 === 0;

    // Print Result
    switch (operator) {
        case "+":
        case "-":
        case "*":
            if (isEven) {
                console.log(`${equation} = ${result} - even`);
            } else {
                console.log(`${equation} = ${result} - odd`);
            }
            break;
        case "/":
            if (num2 === 0){
                console.log(`Cannot divide ${num1} by zero`);
            } else {
                console.log(`${equation} = ${result.toFixed(2)}`);
            }
            break;
        case "%":
            if (num2 === 0){
                console.log(`Cannot divide ${num1} by zero`);
            } else {
                console.log(`${equation} = ${result}`);
            }
            break;
    }
}

operationsBetweenNumbers(["10",
"3",
"%"]);