// Task 8 - Tournament Of Christmas

function tournament(input) {
    // Read Input
    let days = Number(input.shift());

    // Logic
    let totalWins = 0;
    let totalLoses = 0;
    let totalMoney = 0;

    for (let day = 0; day < days; day++) {
        let lost = 0;
        let won = 0;
        let money = 0;

        let sport = input.shift();

        while (sport != "Finish"){
            let winOrLose = input.shift();
            if (winOrLose === "win"){
                totalWins++;
                money += 20;
                won++;
            } else{
                totalLoses++;
                lost++;
            }
            sport = input.shift();
        }
        if (won > lost){
            money += money * 0.10;
        }
        totalMoney += money;
    }

    // Print result
    if (totalWins > totalLoses){
        totalMoney += totalMoney * 0.20;
        console.log(`You won the tournament! Total raised money: ${totalMoney.toFixed(2)}`);
    } else {
        console.log(`You lost the tournament! Total raised money: ${totalMoney.toFixed(2)}`)
    }
}

tournament([
    "3",
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
    "Finish"
]);