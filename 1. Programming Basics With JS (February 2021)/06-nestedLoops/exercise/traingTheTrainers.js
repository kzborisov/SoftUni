// Task 4 - Train The Trainers

function traingTheTrainers(input) {
    // Read Input
    let juryCount = Number(input.shift());
    let presentation = input.shift();

    // Logic
    let totalAverage = 0;
    let count = 0;

    while(presentation != "Finish"){
        let average = 0;
        for (let i = 0; i < juryCount; i++){
            let grade = Number(input.shift());
            average += grade;
            totalAverage += grade;
            count++;
        }
        average /= juryCount;
        console.log(`${presentation} - ${(average).toFixed(2)}.`);

        presentation = input.shift();
    }

    // Print Result
    totalAverage /= count;
    console.log(`Student's final assessment is ${totalAverage.toFixed(2)}.`);
}

traingTheTrainers(["2",
"Objects and Classes",
"5.77",
"4.23",
"Dictionaries",
"4.62",
"5.02",
"RegEx",
"2.88",
"3.42",
"Finish"]);