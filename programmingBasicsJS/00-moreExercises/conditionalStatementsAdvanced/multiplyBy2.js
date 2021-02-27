// Task 10 - Multiply By 2

function pointOnRectangleBorder(input) {
    // Read Input Data
    let num = Number(input[0])
    let result = num * 2;
    console.log(`Result: ${result.toFixed(2)}`)

    // Logic
    let i = 1;
    while (true) {
        let num = Number(input[i]);
        if (num < 0) {
            console.log("Negative number!")
            break;
        }
        let result = num * 2;
        console.log(`Result: ${result.toFixed(2)}`)
        i = i + 1;

    };
}

pointOnRectangleBorder(["23.43", "12.3245", "0", "65.23432", "23", "65", "-12"]);
