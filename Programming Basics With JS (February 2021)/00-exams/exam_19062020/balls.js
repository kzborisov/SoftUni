// Task 4 - Balls

function balls(input) {
    // Read Input Data
    let ballsCount = Number(input.shift());

    // Logic
    let points = 0;
    let counterMap = {
        "Points from red balls: ": 0,
        "Points from orange balls: ": 0,
        "Points from yellow balls: ": 0,
        "Points from white balls: ": 0,
        "Other colors picked: ": 0,
        "Divides from black balls: ": 0
    };

    for (let i = 1; i <= ballsCount; i++) {
        let color = input.shift();

        switch (color) {
            case "red":
                points += 5;
                counterMap["Points from red balls: "]++;
                break;
            case "orange":
                points += 10;
                counterMap["Points from orange balls: "]++;
                break;
            case "yellow":
                points += 15;
                counterMap["Points from yellow balls: "]++;
                break;
            case "white":
                points += 20;
                counterMap["Points from white balls: "]++;
                break;
            case "black":
                points /= 2;
                counterMap["Divides from black balls: "]++;
                break;
            default:
                counterMap["Other colors picked: "]++;
                break;
        }
    }

    // Print Result
    console.log(`Total points: ${Math.floor(points)}`);
    for (key in counterMap){
        console.log(`${key}${counterMap[key]}`);
    }
}

balls(["5",
"red",
"red",
"ddd",
"ddd",
"ddd"]); 