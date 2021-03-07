// Task 6 - Max Number

function maxNumber(input) {

    let max = Number.MIN_SAFE_INTEGER;

    while (true) {
        // Read Input
        let n = input.shift();
        if (n === "Stop"){
            break;
        }
        
        if (Number(n) > max){
            max = n;
        }
    }
    console.log(max);
}

maxNumber(["-1",
"-2",
"Stop"]);