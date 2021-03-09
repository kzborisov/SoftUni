// Task 5 - Best Player

function bestPlayer(input) {
    // Logic
    let i = 0;
    let maxGoals = 0;
    let bestPlayer;

    while (input[i] != "END"){
        let name = input.shift();
        let goals = Number(input.shift());

        if (goals > maxGoals) {
            maxGoals = goals;
            bestPlayer = name;
        }

        if (goals >= 10){
            break;
        }
    }

    // Print Result
    console.log(`${bestPlayer} is the best player!`);
    if (maxGoals >= 3){
        console.log(`He has scored ${maxGoals} goals and made a hat-trick !!!`)
    } else {
        console.log(`He has scored ${maxGoals} goals.`)
    }
}

bestPlayer(["Neymar", "2",
"Ronaldo",
"1",
"Messi",
"3",
"END"]);