// Task 2 - Exam Preparation

function examPreparation(input) {
    // Read Input
    let badGrades = Number(input.shift());

    // Logic
    let average = 0;
    let counter = 0;
    let badGradesCount = 0;
    let lastProblem = "";

    while(true) {
        let task = input.shift();
        let grade = Number(input.shift());

        if(task == "Enough"){
            break;
        }
        if (grade <= 4){
            badGradesCount++;
        }
        if (badGradesCount >= badGrades){
            console.log(`You need a break, ${badGradesCount} poor grades.`);
            return;
        }
        average += grade;
        counter++;
        lastProblem = task;
    }
    console.log(`Average score: ${(average/counter).toFixed(2)}`);
    console.log(`Number of problems: ${counter}`);
    console.log(`Last problem: ${lastProblem}`);
}

examPreparation(["2",
"Income",
"3",
"Game Info",
"6",
"Best Player",
"4"]);