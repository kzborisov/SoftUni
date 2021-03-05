// Task 4 - Grades

function grades(input) {
    // Read Input
    let studentsCount = Number(input[0]);

    // Logic
    let gradeMap = {
        'Top students:': 0,
        'Between 4.00 and 4.99:': 0,
        'Between 3.00 and 3.99:': 0,
        'Fail:': 0
    };
    let totalGradesCount = 0;
    let average = 0;

    for (let i = 1; i <= studentsCount; i++) {
        let grade = Number(input[i]);
        totalGradesCount++;
        average += grade;

        if (grade >= 5){
            gradeMap['Top students:']++;
        } else if (grade >= 4){
            gradeMap['Between 4.00 and 4.99:']++;
        } else if (grade >= 3){
            gradeMap['Between 3.00 and 3.99:']++;
        } else {
            gradeMap['Fail:']++;
        }
    }

    // Print Result
    for(let key in gradeMap){
        console.log(`${key} ${(gradeMap[key]/totalGradesCount*100).toFixed(2)}%`);
    }
    console.log(`Average: ${(average/totalGradesCount).toFixed(2)}`);
}

grades(["10", "3.00", "2.99", "5.68", "3.01", "4", "4", "6.00", "4.50", "2.44", "5"]);