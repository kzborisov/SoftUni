// Task 5 - Game Of Intervals

function gameOfIntervals(input) {
    // Read Input
    let movesCount = Number(input[0]);

    // Logic
    let totalPoints = 0;
    let totalPointsCount = 0;

    let pointsMap = {
        "From 0 to 9:": 0,
        "From 10 to 19:": 0,
        "From 20 to 29:": 0,
        "From 30 to 39:": 0,
        "From 40 to 50:": 0,
        "Invalid numbers:": 0
    };

    for (let i = 1; i <= movesCount; i++){
        let num = Number(input[i]);

        if (num > 50 || num < 0) {
            pointsMap["Invalid numbers:"]++;
            totalPoints /= 2;
        } else if (num >= 40){
            pointsMap["From 40 to 50:"]++;
            totalPoints += 100;
        } else if (num >= 30) {
            pointsMap["From 30 to 39:"]++;
            totalPoints += 50;
        } else if (num >= 20){
            pointsMap["From 20 to 29:"]++;
            totalPoints += num * 0.40;
        } else if (num >= 10){
            pointsMap["From 10 to 19:"]++;
            totalPoints += num * 0.30;
        }else if(num >= 0){
            pointsMap["From 0 to 9:"]++;
            totalPoints += num * 0.20;
        }
    }

    // Print Result
    console.log(totalPoints.toFixed(2));
    for(key in pointsMap){
        console.log(`${key} ${(pointsMap[key]/movesCount*100).toFixed(2)}%`);
    }
}

gameOfIntervals(["10",
"43",
"57",
"-12",
"23",
"12",
"0",
"50",
"40",
    "30",
    "20"]);