// Task 2 - Multiplication Table

function multiplicationTable() {
    for (var first = 1; first <= 10; first++){
        for (var second = 1; second <= 10; second++){
            let result = first * second;
            console.log(`${first} * ${second} = ${result}`);
        }
    }
}

multiplicationTable()