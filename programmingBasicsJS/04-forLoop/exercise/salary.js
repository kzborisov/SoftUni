// Task 8 - Salary

function salary(input) {
    // Read Input
    let tabsOpened = Number(input[0]);
    let income = Number(input[1]);

    // Logic
    for (let i=2; i <= tabsOpened+1; i++) {
        let tab = input[i];

        if (tab === "Facebook"){
            income -= 150;
        } else if (tab === "Instagram"){
            income -= 100;
        } else if (tab === "Reddit"){
            income -= 50;
        }

        if (income <= 0){
            console.log("You have lost your salary.")
            return;
        }
    }

    // Print result
    console.log(income.toFixed(0));
}

salary(["3",
"500",
"Github.com",
"Stackoverflow.com",
"softuni.bg"]);