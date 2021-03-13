// Task 5 - Traveling

function traveling(input) {
    // Read Input
    let destination = input.shift();

    // Logic
    while (destination != "End"){
        let price = input.shift();
        let savedMoney = 0;
        while (savedMoney < price){
            savedMoney += Number(input.shift());
        }
        console.log(`Going to ${destination}!`);
        destination = input.shift();
    }
}

traveling(["Greece",
"1000",
"200",
"200",
"300",
"100",
"150",
"240",
"Spain",
"1200",
"300",
"500",
"193",
"423",
"End"]);