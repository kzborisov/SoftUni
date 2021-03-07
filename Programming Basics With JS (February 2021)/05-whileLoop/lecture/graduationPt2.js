// Task 8 - Graduation Pt. 2

function graduation(input) {
    let name = input.shift();

    let average = 0;
    let counter = 0;
    let isGraduation = true;
    let failCount = 0;

    while (input.length > 0) {
        let grade = Number(input.shift());
        average += grade;
        counter++;

        if (grade < 4 ){
            failCount++;
        }

        if (failCount >= 2) {
            isGraduation = false;
            break;
        }
    }

    if (isGraduation) {
        average /= counter;
        console.log(`${name} graduated. Average grade: ${average.toFixed(2)}`)
    } else {
        console.log(`${name} has been excluded at ${counter-1} grade`)
    }
}

graduation(["Gosho", 
"5",
"5.5",
"6",
"5.43",
"5.5",
"6",
"5.55",
"5",
"6",
"6",
"5.43",
"5"]);