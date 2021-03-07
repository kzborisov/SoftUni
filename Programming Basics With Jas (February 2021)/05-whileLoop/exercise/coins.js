// Task 5 - Coins *

function coins(input) {
    let change = Math.round(input.shift() * 100);
    let coins = 0;

    while (change > 0){
        if (change >= 200){
            change -= 200;
            coins++;
        } else if (change >= 100){
            change -= 100;
            coins++;
        } else if (change >= 50){
            change -= 50;
            coins++;
        } else if (change >= 20){
            change -= 20;
            coins++;
        } else if (change >= 10){
            change -= 10;
            coins++;
        } else if (change >= 5){
            change -= 5;
            coins++;
        } else if (change >= 2){
            change -= 2;
            coins++;
        } else {
            change -= 1;
            coins++;
        }
    }
    console.log(coins);
}

coins(["1.51"]);