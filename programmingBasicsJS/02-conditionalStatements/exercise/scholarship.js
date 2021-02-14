// Task 8 - Scholarship

function scholarship(input) {
    // Read Input Data
    let income = Number(input[0]);
    let average = Number(input[1]);
    let minimalWage = Number(input[2]);

    let isSocial;
    let socialMoney;
    let isGrade;
    let goodGradeMoney;

    // Calculations

    // Social Scholarship
    if (income <= minimalWage && average >= 4.5) {
        isSocial = true;
    }

    // Excelent Grade Scholarship
    if (average >= 5.5) {
        isGrade = true;
    }

    socialMoney = minimalWage * 0.35;
    goodGradeMoney = average * 25;

    // Print result
    if (isSocial && isGrade) {
        if (goodGradeMoney >= socialMoney) {
            console.log(`You get a scholarship for excellent results ${Math.floor(goodGradeMoney)} BGN`)
        } else {
            console.log(`You get a Social scholarship ${Math.floor(socialMoney)} BGN`)
        }
    } else if (isGrade) {
        console.log(`You get a scholarship for excellent results ${Math.floor(goodGradeMoney)} BGN`)
    } else if (isSocial) {
        console.log(`You get a Social scholarship ${Math.floor(socialMoney)} BGN`)
    } else {
        console.log("You cannot get a scholarship!")
    }

}

scholarship(["480.00",
"4.60",
"450.00"]);