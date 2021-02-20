// Task 12- Trade Commissions

function tradeCommission(input) {
    // Read Input Data
    let town = input[0];
    let sales = Number(input[1]);

    // Calculations
    let commission;
    if (town === "Sofia") {
        if (sales >= 0 && sales <= 500){
            commission = sales * 0.05;
        } else if (sales > 500 && sales <= 1000){
            commission = sales * 0.07;
        } else if (sales > 1000 && sales <= 10000){
            commission = sales * 0.08;
        } else if (sales > 10000){
            commission = sales * 0.12;
        }else {
            console.log("error");
            return;
        }
    } else if (town === "Varna") {
        if (sales >= 0 && sales <= 500){
            commission = sales * 0.045;
        } else if (sales > 500 && sales <= 1000){
            commission = sales * 0.075;
        } else if (sales > 1000 && sales <= 10000){
            commission = sales * 0.10;
        } else if (sales > 10000){
            commission = sales * 0.13;
        }else {
            console.log("error");
            return;
        }
    } else if (town === "Plovdiv") {
        if (sales >= 0 && sales <= 500){
            commission = sales * 0.055;
        } else if (sales > 500 && sales <= 1000){
            commission = sales * 0.08;
        } else if (sales > 1000 && sales <= 10000){
            commission = sales * 0.12;
        } else if (sales > 10000){
            commission = sales * 0.145;
        }else {
            console.log("error");
            return;
        }
    } else {
        console.log("error");
        return;
    }

    // Print Result
    console.log(commission.toFixed(2));
}

tradeCommission((["Kaspichan",
"-50"]));
