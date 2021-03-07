// Task 7 - Min Number

function minNumber(input) {

    let min = Number.MAX_SAFE_INTEGER;

    while (true) {
        // Read Input
        let n = input.shift();
        if (n === "Stop"){
            break;
        }
        
        if (Number(n) < min){
            min = n;
        }
    }
    console.log(min);
}

minNumber(["100",
"99",
"80",
"70",
"Stop"]);