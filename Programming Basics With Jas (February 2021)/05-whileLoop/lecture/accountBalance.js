// Task 5 - Account Balance

function accountBalance(input) {
    // Logic
    let balance = 0;
    let deposit = input.shift();

    while(deposit != "NoMoreMoney"){
        let currentAmount = Number(deposit);

        if (currentAmount < 0){
            console.log("Invalid operation!");
            break;
        }

        balance += currentAmount;
        console.log(`Increase: ${currentAmount.toFixed(2)}`);

        deposit = input.shift();
    }
    console.log(`Total: ${Number(balance).toFixed(2)}`);
}

accountBalance(["120",
"45.55",
"-150"]);