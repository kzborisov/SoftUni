// Task 1 - Numbers Ending in 7

function numbersEndingIn7() {
    // Logic
    for (var i = 7; i < 1000; i++){
        if (i % 10 == 7){
            console.log(i);
        }
    }
}

numbersEndingIn7()