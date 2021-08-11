// Task 12 - Tournament of Christmas 

function tournament(input) {
    // Read Input
    let days = Number(input.shift());

    // Logic
    let money = 0;
    let winningDays = 0;
    let losingDays = 0;

    for (let day = 1; day <= days; day++) {
        let moneyPerDay = 0;
        let wins = 0;
        let loses = 0;
        let sport = input.shift();

        while (sport !== "Finish"){
            let result = input.shift();

            if(result === "win"){
                moneyPerDay += 20;
                wins++;
            } else {
                loses++;
            }

            sport = input.shift();
        }

        if(wins > loses){
            moneyPerDay += moneyPerDay * 0.10;
            winningDays++;
        }
        else{
            losingDays++;
        }

        money += moneyPerDay;
    }

    // Print Result
    if (winningDays > losingDays){
        money += money * 0.20;
        console.log(`You won the tournament! Total raised money: ${money.toFixed(2)}`);
    } else {
        console.log(`You lost the tournament! Total raised money: ${money.toFixed(2)}`);
    }
}

tournament(["3",
"darts",
"lose",
"handball",
"lose",
"judo",
"win",
"Finish",
"snooker",
"lose",
"swimming",
"lose",
"squash",
"lose",
"table tennis",
"win",
"Finish",
"volleyball",
"win",
"basketball",
"win",
"Finish"])
;