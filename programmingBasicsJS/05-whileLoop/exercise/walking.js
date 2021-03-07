// Task 4 - Walking

function walking(input) {

    let totalSteps = 0;
    let command = input.shift();

    while (totalSteps < 10000 && command !== 'Going home') {
        let steps = Number(command);
        totalSteps += steps;
        command = input.shift();
    }

    if (command === 'Going home') {
        let finalSteps = Number(input.shift());
        totalSteps += finalSteps;
    }

    if (totalSteps < 10000) {
        let finalResult = 10000 - totalSteps;
        console.log(`${finalResult} more steps to reach goal.`);
    } else {
        console.log('Goal reached! Good job!');
        let finalResult = totalSteps - 10000;
        console.log(`${finalResult} steps over the goal!`);
    }
}

walking(["125",
"250",
"4000",
"30",
"2678",
"4682"]);