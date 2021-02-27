// Task 4 - Even Powers of 2

function evenPowersOf2(input) {
    // Read Input
    let num = Number(input[0]);

    // Print Even Numbers of 2
    for (var i = 0; i <= num; i+=2) {
        console.log(Math.pow(2, i));
    }
}

evenPowersOf2(['7'])