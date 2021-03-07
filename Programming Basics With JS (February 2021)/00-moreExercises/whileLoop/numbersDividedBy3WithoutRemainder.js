// Task 4 - Numbers Divided By 3 Without Remainder

function dividedBy3(input) {
    let n = 1;
    while(n < 100){
        if (n % 3 == 0){
            console.log(n);
        }
        n++;
    } 
}

dividedBy3();