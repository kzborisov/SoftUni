// Task 3 - Vacation

function vacation(input) {
    // Read Input
    let neededMoney = Number(input.shift());
    let currentMoney = Number(input.shift());

    // Logic
    let counter = 0;
    let counterSpend = 0;

    while (true) {
        let action = input.shift();
        let sum = Number(input.shift());
        counter++;

        switch (action) {
            case "spend":
                currentMoney -= sum;
                if (currentMoney < 0){
                    currentMoney = 0;
                }
                counterSpend++;
                break;
            case "save":
                currentMoney += sum;
                counterSpend = 0;
                break;
        }
        if (counterSpend >= 5){
            console.log(`You can't save the money.`);
            console.log(counter);
            break;
        }
        if (currentMoney >= neededMoney){
            console.log(`You saved the money for ${counter} days.`);
        }
        if (input.length < 1){
            break;
        }
    }
}

vacation(["2000",
"1000",
"spend",
"1200",
"save",
"2000"]);